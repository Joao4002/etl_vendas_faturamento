import pandas as pd
import pyodbc

def load_vendas(df: pd.DataFrame, caminho_destino: str):
    """
    Carrega os dados tratados no SQL Server
    e salva o CSV final (opcional).
    """

    # =========================
    # 1. Salvar CSV tratado
    # =========================
    df.to_csv(caminho_destino, index=False)
    print(f"Arquivo salvo em: {caminho_destino}")

    # =========================
    # 2. Conexão com SQL Server
    # =========================
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-I3OBPJD9\\SQLEXPRESS;"
        "DATABASE=etl_vendas_faturamento;"
        "Trusted_Connection=yes;"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # =========================
    # 3. Inserção dos dados
    # =========================
    insert_sql = """
    INSERT INTO vendas_faturamento
    (id_venda, [data], produto, quantidade, preco_unitario, faturamento)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    for _, row in df.iterrows():
        cursor.execute(
            insert_sql,
            int(row["id_venda"]),
            row["data"],
            row["produto"],
            int(row["quantidade"]),
            float(row["preco_unitario"]),
            float(row["faturamento"])
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Dados carregados com sucesso no SQL Server.")
