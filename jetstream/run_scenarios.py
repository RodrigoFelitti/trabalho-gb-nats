"""
Runner dos cenários de teste para o NATS JetStream.

Mesmos cenários do Core + um cenário extra de replicação (R=1 vs R=3).
Resultados salvos em results/ no formato combinado.

TODO (Pessoa 2):
- Reaproveitar o máximo possível os módulos de app/
- Cenário 'replicacao': rodar o Cenário 1 com R=1 e depois R=3, comparar
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import sensor, consumer, alert_service, config


async def cenario_vazao():
    """TODO: idem Core, mas publicando/consumindo via JetStream."""
    raise NotImplementedError


async def cenario_escalabilidade():
    """TODO: idem Core, mas em JetStream."""
    raise NotImplementedError


async def cenario_resiliencia():
    """TODO: esperado zero perda após a volta do consumer."""
    raise NotImplementedError


async def cenario_replicacao():
    """TODO: rodar Cenário 1 com R=1 e com R=3, comparar latência."""
    raise NotImplementedError


CENARIOS = {
    "vazao": cenario_vazao,
    "escalabilidade": cenario_escalabilidade,
    "resiliencia": cenario_resiliencia,
    "replicacao": cenario_replicacao,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cenario", required=True, choices=CENARIOS.keys())
    args = parser.parse_args()
    asyncio.run(CENARIOS[args.cenario]())
