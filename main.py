from src.extract import extract_vendas
from src.transform import transform_vendas
from src.load import load_vendas

CAMINHO_CSV_RAW = "data/raw/vendas.csv"
CAMINHO_CSV_TRATADO = "data/processed/vendas_tratadas.csv"

from src.extract import extract_vendas
from src.transform import transform_vendas
from src.load import load_vendas

def main():
    # === ETAPA 1: EXTRAÇÃO ===
    df_vendas = extract_vendas("data/raw/vendas.csv")
    print("=== Dados Extraídos ===")
    print(df_vendas)

    # === ETAPA 2: TRANSFORMAÇÃO ===
    df_vendas_tratada = transform_vendas(df_vendas)
    print("\n=== Dados Transformados ===")
    print(df_vendas_tratada)

    # === ETAPA 3: RESUMO DE FATURAMENTO ===
    resumo_total = df_vendas_tratada['faturamento'].sum()
    print(f"\nFaturamento total: R$ {resumo_total}")

    resumo_produto = df_vendas_tratada.groupby('produto')['faturamento'].sum()
    print("\nFaturamento por produto:")
    print(resumo_produto)

    # === ETAPA 4: CARGA ===
    arquivo_saida = "data/processed/vendas_tratadas.csv"
    load_vendas(df_vendas_tratada, arquivo_saida)
    print(f"\nArquivo salvo em: {arquivo_saida}")

if __name__ == "__main__":
    main()
