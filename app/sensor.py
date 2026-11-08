"""
Sensor simulado — publisher.

Publica leituras periódicas em `sensores.<id>.leitura`.
Deve funcionar tanto contra NATS Core (publish simples) quanto contra
JetStream (publish em stream) — a diferença fica no runner que chama este módulo.

TODO (Pessoa 1 e 2):
- Implementar função `run_sensor(sensor_id, taxa_hz, duracao_s, tamanho_payload)`
- Payload JSON: {"id": sensor_id, "valor": float, "timestamp": ISO8601, "padding": "..." para atingir tamanho}
- Suportar modo core (nc.publish) e modo jetstream (js.publish)
- Instrumentar envio para o CSV combinado no CONTRATO.md
"""

import asyncio
import json
import random
import time
from datetime import datetime, timezone

import nats

from app import config

async def esperar_ate(momento: float):
    """Dorme até o cronômetro chegar em `momento`."""
    falta = momento - time.perf_counter()
    if falta > 0:
        await asyncio.sleep(falta)

def cria_mensagem(sensor_id: str, tamanho: int) -> bytes:
    """Monta uma leitura em JSON com exatamente `tamanho` bytes."""
    dados = {
        "id": sensor_id,
        "valor": round(random.uniform(0, 100), 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "padding": "",
    }

    tamanho_base = len(json.dumps(dados).encode())
    dados["padding"] = "x" * (tamanho - tamanho_base)

    return json.dumps(dados).encode()

async def run_sensor(sensor_id: str, taxa_hz: int, duracao_s: int, tamanho_payload: int, modo: str):
    """Executa um sensor que publica leituras."""
    conn = await nats.connect(config.NATS_URL_LOCAL)

    total_msgs = taxa_hz * duracao_s
    inicio = time.perf_counter()
    intervalo = 1 / taxa_hz

    for i in range(total_msgs):
        await esperar_ate(inicio + i * intervalo)

        msg = cria_mensagem(sensor_id, tamanho_payload)
        await conn.publish(config.SUBJECT_SENSOR.format(sensor_id=sensor_id), msg)

    await conn.drain()
