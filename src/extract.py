import pandas as pd

def extract_vendas(caminho_csv: str) -> pd.DataFrame:
    """
    Lê o arquivo CSV de vendas e retorna um DataFrame.
    """
    df = pd.read_csv(caminho_csv)
    return df
