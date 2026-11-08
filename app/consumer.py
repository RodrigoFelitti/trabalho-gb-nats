"""
Consumer — subscriber que processa leituras dos sensores.

Assina `sensores.>` e processa cada mensagem. Mede latência fim-a-fim
comparando timestamp do payload com o momento da recepção.

Pode operar em queue group (para o cenário de escalabilidade).

Devolve a latência de cada mensagem; quem grava o CSV é o runner.

Falta (Pessoa 2): suportar modo jetstream (js.subscribe com consumer).
"""

import asyncio
import json
from datetime import datetime, timezone

import nats

from app import config

async def run_consumer(modo: str, duracao_s: float, queue_group: str = None,
                       com_alerta: bool = False) -> list[float]:
    """Executa um consumer e devolve a latência (ms) de cada mensagem recebida."""
    conn = await nats.connect(config.NATS_URL_LOCAL)

    latencias = []

    async def recebe_msg(msg):
        agora = datetime.now(timezone.utc)
        dados = json.loads(msg.data)
        timestamp = datetime.fromisoformat(dados["timestamp"])
        latencia = (agora - timestamp).total_seconds() * 1000
        latencias.append(latencia)

        if com_alerta:
            asyncio.create_task(conn.request(config.SUBJECT_ALERTA_REQUEST, msg.data))

    await conn.subscribe(config.SUBJECT_SENSOR_WILDCARD, queue=queue_group, cb=recebe_msg)
    await asyncio.sleep(duracao_s)
    await conn.drain()

    return latencias
