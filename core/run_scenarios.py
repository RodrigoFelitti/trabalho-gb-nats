"""
Runner dos cenários de teste para o NATS Core.

Orquestra sensores, consumers e serviço de alerta para executar
cada um dos cenários-base do CONTRATO.md.

TODO (Pessoa 1):
- Cenário 'vazao': 1 publisher, 1 subscriber, variar tamanho (100B, 1KB, 10KB)
- Cenário 'escalabilidade': variar nº publishers (1, 10, 50), 3 subs em queue group
- Cenário 'resiliencia': publisher a 500 msg/s por 60s, derrubar sub nos s 20-50
- Gerar CSV em results/ no formato combinado
"""

import argparse
import asyncio
import csv
import json
import sys
from pathlib import Path

import nats

# Permitir importar da pasta app/
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import sensor, consumer, alert_service, config

COLUNAS = ["cenario", "modo", "tamanho_msg", "n_publishers", "n_subscribers",
           "latencia_ms", "msg_enviadas", "msg_recebidas", "duracao_s"]


def salvar_csv(linhas, nome_arquivo):
    caminho = Path(__file__).parent / "results" / nome_arquivo
    with open(caminho, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(COLUNAS)
        escritor.writerows(linhas)


async def cenario_vazao():
    """1 pub + 1 sub, variar tamanho de msg."""
    linhas = []

    for tamanho in [100, 1000, 10000]:
        tarefa = asyncio.create_task(consumer.run_consumer("core", duracao_s=61))
        await asyncio.sleep(0.5)

        await sensor.run_sensor("sensor-1", taxa_hz=1000, duracao_s=60,
                                tamanho_payload=tamanho, modo="core")

        latencias = await tarefa
        for lat in latencias:
            linhas.append(["vazao", "core", tamanho, 1, 1, lat, 60000, len(latencias), 60])

    salvar_csv(linhas, "resultados_core_vazao.csv")


async def cenario_escalabilidade():
    """N pubs, 3 subs em queue group."""
    linhas = []

    for n_pubs in [1, 10, 50]:
        consumers = [asyncio.create_task(consumer.run_consumer("core", duracao_s=61, queue_group="processadores"))
                     for _ in range(3)]
        await asyncio.sleep(0.5)

        sensores = [sensor.run_sensor(f"sensor-{i}", taxa_hz=500, duracao_s=60,
                                      tamanho_payload=1000, modo="core")
                    for i in range(n_pubs)]
        await asyncio.gather(*sensores)

        latencias = []
        for c in consumers:
            latencias += await c

        for lat in latencias:
            linhas.append(["escalabilidade", "core", 1000, n_pubs, 3, lat,
                           500 * 60 * n_pubs, len(latencias), 60])

    salvar_csv(linhas, "resultados_core_escalabilidade.csv")


async def cenario_resiliencia():
    """1 pub a 500 msg/s por 60s, derrubar sub nos s 20-50."""
    antes_da_queda = asyncio.create_task(consumer.run_consumer("core", duracao_s=20.5))
    await asyncio.sleep(0.5)

    tarefa_sensor = asyncio.create_task(sensor.run_sensor("sensor-1", taxa_hz=500, duracao_s=60,
                                                          tamanho_payload=1000, modo="core"))

    latencias_antes = await antes_da_queda
    await asyncio.sleep(30)
    latencias_depois = await consumer.run_consumer("core", duracao_s=10.5)

    await tarefa_sensor

    latencias = latencias_antes + latencias_depois

    linhas = []
    for lat in latencias:
        linhas.append(["resiliencia", "core", 1000, 1, 1, lat, 500 * 60, len(latencias), 60])

    salvar_csv(linhas, "resultados_core_resiliencia.csv")


async def cenario_alerta():
    """Demonstração do request/reply com o serviço de alerta (não gera CSV)."""
    servico = asyncio.create_task(alert_service.run_alert_service("core", duracao_s=3))
    await asyncio.sleep(0.5)

    conn = await nats.connect(config.NATS_URL_LOCAL)
    for valor in [50.0, 85.0, 95.0]:
        resposta = await conn.request(config.SUBJECT_ALERTA_REQUEST,
                                      json.dumps({"valor": valor}).encode())
        print(f"valor {valor}: {resposta.data.decode()}")
    await conn.drain()

    await servico


CENARIOS = {
    "vazao": cenario_vazao,
    "escalabilidade": cenario_escalabilidade,
    "resiliencia": cenario_resiliencia,
    "alerta": cenario_alerta,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cenario", required=True, choices=CENARIOS.keys())
    args = parser.parse_args()
    asyncio.run(CENARIOS[args.cenario]())
