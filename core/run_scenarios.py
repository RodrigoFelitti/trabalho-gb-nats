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
import sys
from pathlib import Path

# Permitir importar da pasta app/
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import sensor, consumer, alert_service, config


async def cenario_vazao():
    """TODO: 1 pub + 1 sub, variar tamanho de msg."""
    raise NotImplementedError


async def cenario_escalabilidade():
    """TODO: N pubs, 3 subs em queue group."""
    raise NotImplementedError


async def cenario_resiliencia():
    """TODO: 1 pub a 500 msg/s por 60s, derrubar sub nos s 20-50."""
    raise NotImplementedError


CENARIOS = {
    "vazao": cenario_vazao,
    "escalabilidade": cenario_escalabilidade,
    "resiliencia": cenario_resiliencia,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cenario", required=True, choices=CENARIOS.keys())
    args = parser.parse_args()
    asyncio.run(CENARIOS[args.cenario]())
