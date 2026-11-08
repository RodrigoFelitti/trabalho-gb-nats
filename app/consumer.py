"""
Consumer — subscriber que processa leituras dos sensores.

Assina `sensores.>` e processa cada mensagem. Mede latência fim-a-fim
comparando timestamp do payload com o momento da recepção.

Suporta modo core (nc.subscribe) e modo jetstream (js.subscribe com consumer).

Pode operar em queue group (para o cenário de escalabilidade).

TODO (Pessoa 1 e 2):
- Implementar função `run_consumer(modo, duracao_s, queue_group=None, com_alerta=False)`
- Devolver a latência de cada mensagem (o runner grava o CSV combinado, ver CONTRATO.md)
- Suportar ser derrubado graciosamente (SIGTERM) para o teste de resiliência
"""

import asyncio
import nats
import json
from datetime import datetime, timezone
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
