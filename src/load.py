import pandas as pd

def load_vendas(df: pd.DataFrame, caminho_destino: str):
    """
    Salva o DataFrame transformado em um arquivo CSV.
    """
    df.to_csv(caminho_destino, index=False)
    print(f"Arquivo salvo em: {caminho_destino}")
