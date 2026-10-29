"""
Serviço de alerta — request/reply.

Exercita o padrão request/reply do NATS (seção 3.3 do artigo do GA).
O consumer, ao receber uma leitura acima do limite, faz request para
`alertas.verificar` e este serviço responde se deve disparar alerta ou não.

TODO (Pessoa 1 e 2):
- Implementar função `run_alert_service(modo)`
- Assinar SUBJECT_ALERTA_REQUEST e responder via reply inbox
- Lógica simples: se valor > LIMITE_ALERTA, responde {"alerta": true}
"""

import asyncio
import nats


async def run_alert_service(modo: str):
    """Executa o serviço de alerta."""
    # TODO: implementar
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: parse argumentos CLI
    pass
