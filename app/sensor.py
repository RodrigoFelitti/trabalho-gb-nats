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
import nats


async def run_sensor(sensor_id: str, taxa_hz: int, duracao_s: int, tamanho_payload: int, modo: str):
    """Executa um sensor que publica leituras."""
    # TODO: implementar
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: parse argumentos CLI
    pass
