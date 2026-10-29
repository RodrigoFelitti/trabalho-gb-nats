"""
Setup inicial dos streams e consumers do JetStream.

Deve ser executado uma vez antes dos cenários. Pode receber um parâmetro
para o fator de replicação (R=1 ou R=3) usado no cenário extra.

TODO (Pessoa 2):
- Conectar ao cluster
- Criar o stream SENSORES capturando subject sensores.>
- Definir política de retenção (ex: WorkQueue ou Limits com max_msgs)
- Criar consumer durável
- Suportar flag --replicas (1 ou 3) para o cenário de replicação
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import config


async def setup(replicas: int = 1):
    """Cria stream e consumer no cluster JetStream."""
    # TODO: implementar
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--replicas", type=int, default=1, choices=[1, 3])
    args = parser.parse_args()
    asyncio.run(setup(args.replicas))
