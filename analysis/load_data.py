"""
Carrega os CSVs gerados pelas Pessoas 1 e 2 em DataFrames pandas.

Esperamos CSVs no formato definido no CONTRATO.md:
cenario, modo, tamanho_msg, n_publishers, n_subscribers,
latencia_ms, msg_enviadas, msg_recebidas, duracao_s

TODO (Pessoa 3):
- Carregar todos os CSVs de ../core/results/ e ../jetstream/results/
- Concatenar em um único DataFrame
- Expor funções auxiliares para filtrar por cenário/modo
"""

from pathlib import Path
import pandas as pd

CORE_RESULTS_DIR = Path(__file__).parent.parent / "core" / "results"
JETSTREAM_RESULTS_DIR = Path(__file__).parent.parent / "jetstream" / "results"


def load_all() -> pd.DataFrame:
    """Carrega todos os CSVs e retorna um DataFrame único."""
    dfs = []
    for csv in list(CORE_RESULTS_DIR.glob("*.csv")) + list(JETSTREAM_RESULTS_DIR.glob("*.csv")):
        dfs.append(pd.read_csv(csv))
    if not dfs:
        raise FileNotFoundError("Nenhum CSV encontrado — rode os cenários primeiro.")
    return pd.concat(dfs, ignore_index=True)


if __name__ == "__main__":
    df = load_all()
    print(df.head())
    print(f"\nTotal de linhas: {len(df)}")
    print(f"Cenários: {df['cenario'].unique()}")
    print(f"Modos: {df['modo'].unique()}")
