"""
Consumer — subscriber que processa leituras dos sensores.

Assina `sensores.>` e processa cada mensagem. Mede latência fim-a-fim
comparando timestamp do payload com o momento da recepção.

Suporta modo core (nc.subscribe) e modo jetstream (js.subscribe com consumer).

Pode operar em queue group (para o cenário de escalabilidade).

TODO (Pessoa 1 e 2):
- Implementar função `run_consumer(modo, queue_group=None, output_csv=None)`
- Registrar latência de cada mensagem no CSV combinado (ver CONTRATO.md)
- Suportar ser derrubado graciosamente (SIGTERM) para o teste de resiliência
"""

import asyncio
import nats


async def run_consumer(modo: str, queue_group: str = None, output_csv: str = None):
    """Executa um consumer que processa leituras."""
    # TODO: implementar
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: parse argumentos CLI
    pass
