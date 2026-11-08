"""
Serviço de alerta — request/reply.

Exercita o padrão request/reply do NATS (seção 3.3 do artigo do GA).
Quem pergunta faz request para `alertas.verificar` e este serviço responde
se deve disparar alerta ou não. Nos cenários de medição fica desligado por
padrão (ver `com_alerta` no consumer e o cenário 'alerta' no runner).
"""

import asyncio
import json

import nats

from app import config


async def run_alert_service(modo: str, duracao_s: float):
    """Executa o serviço de alerta."""
    conn = await nats.connect(config.NATS_URL_LOCAL)

    async def responde(msg):
        dados = json.loads(msg.data)
        resposta = {"alerta": dados["valor"] > config.LIMITE_ALERTA}
        await msg.respond(json.dumps(resposta).encode())

    await conn.subscribe(config.SUBJECT_ALERTA_REQUEST, cb=responde)
    await asyncio.sleep(duracao_s)
    await conn.drain()
