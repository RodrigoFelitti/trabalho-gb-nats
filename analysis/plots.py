"""
Geração dos gráficos comparativos Core vs JetStream.

TODO (Pessoa 3):
- plot_latencia(): barras p50/p99 Core vs JetStream por tamanho de msg
- plot_vazao(): linhas de vazão por nº publishers, Core vs JetStream
- plot_resiliencia(): barras lado a lado enviadas vs recebidas em cada modo
- plot_replicacao(): comparação R=1 vs R=3 no JetStream
- Salvar tudo em output/ em PNG, com DPI alto para o artigo
"""

from pathlib import Path
import matplotlib.pyplot as plt

from load_data import load_all

OUTPUT_DIR = Path(__file__).parent / "output"


def plot_latencia(df):
    """TODO."""
    raise NotImplementedError


def plot_vazao(df):
    """TODO."""
    raise NotImplementedError


def plot_resiliencia(df):
    """TODO."""
    raise NotImplementedError


def plot_replicacao(df):
    """TODO."""
    raise NotImplementedError


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = load_all()
    plot_latencia(df)
    plot_vazao(df)
    plot_resiliencia(df)
    plot_replicacao(df)
    print(f"Gráficos salvos em {OUTPUT_DIR}")
