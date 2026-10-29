"""
Gera a tabela resumo comparativa Core vs JetStream.

TODO (Pessoa 3):
- Agregar métricas: latência p50/p99, vazão sustentada, taxa de perda
- Exportar como LaTeX (output/tabela_resumo.tex) para incluir no artigo
- Também imprimir no console para conferência rápida
"""

from pathlib import Path

from load_data import load_all

OUTPUT_DIR = Path(__file__).parent / "output"


def build_summary(df):
    """Agrega resultados em tabela resumo."""
    # TODO: implementar
    raise NotImplementedError


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = load_all()
    summary = build_summary(df)
    print(summary)
