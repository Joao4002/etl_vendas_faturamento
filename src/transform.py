import pandas as pd

def transform_vendas(df):
    """
    Aplica regras de negócio aos dados de vendas:
    1. Padroniza datas para YYYY-MM-DD
    2. Remove vendas com quantidade <= 0
    3. Calcula faturamento = quantidade * preco_unitario
    4. Exibe quantidade de linhas removidas
    """

    # Contar linhas originais
    linhas_iniciais = len(df)

    # Normalizar separadores de data para "/"
    df['data'] = df['data'].astype(str).str.replace(r'[-.]', '/', regex=True)

    # Converter para datetime
    df['data'] = pd.to_datetime(df['data'], dayfirst=True, errors='coerce')

    # Remover vendas com quantidade <= 0
    df = df[df['quantidade'] > 0].copy()

    # Calcular faturamento
    df['faturamento'] = df['quantidade'] * df['preco_unitario']

    # Contar linhas removidas
    linhas_removidas = linhas_iniciais - len(df)
    print(f"{linhas_removidas} vendas removidas por quantidade inválida")

    # Garantir que todas as datas fiquem em formato YYYY-MM-DD
    df['data'] = df['data'].dt.strftime('%Y-%m-%d')

    return df
