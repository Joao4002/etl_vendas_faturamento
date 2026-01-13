# ETL de Vendas/Faturamento 

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-green)

---

##  Sobre o Projeto

Este projeto implementa um **pipeline ETL em Python** para processar dados de vendas.  
O objetivo é extrair os dados de um arquivo CSV, aplicar **regras de negócio** e salvar os dados tratados para análise de faturamento.

O pipeline realiza:  
-  **Extração** dos dados do CSV  
-  **Transformação e limpeza** (remoção de vendas inválidas, padronização de datas, cálculo de faturamento)  
-  **Carga** dos dados tratados em um CSV final  

---

## 🗂 Estrutura do Projeto

etl_vendas_faturamento/
├── data/
│ ├── raw/ # CSVs de entrada
│ │ └── vendas.csv
│ └── processed/ # CSVs processados
│ └── vendas_tratadas.csv
├── src/
│ ├── extract.py # Função de extração
│ ├── transform.py # Função de transformação
│ └── load.py # Função de carga (salvar CSV)
├── main.py # Executa o pipeline ETL
├── requirements.txt # Dependências do projeto
└── README.md



---

##  Tecnologias Usadas

* Python 3.13  
* Pandas 2.3.3

---

##  Como Rodar

1. Instale as dependências:

pip install -r requirements.txt

2. Execute o pipeline:

python main.py

---

## Regras de Negócio Aplicadas

1. Remover vendas com quantidade ≤ 0

2. Padronizar datas para o formato YYYY-MM-DD

3. Calcular faturamento = quantidade × preco_unitario

4. Exibir no terminal:
-Quantidade de vendas removidas
-Faturamento total
-Faturamento por produto


---

## Exemplo de Entrada (vendas.csv)

| id_venda | data       | produto  | quantidade | preco_unitario |
| -------- | ---------- | -------- | ---------- | -------------- |
| 1        | 2024/01/05 | Notebook | 2          | 3500           |
| 2        | 05-01-2024 | Mouse    | 0          | 50             |
| 3        | 2024-01-06 | Teclado  | 1          | 150            |
| 4        | 06/01/2024 | Monitor  | -1         | 1200           |
| 5        | 2024.01.07 | Cadeira  | 3          | 800            |



---

## Exemplo de Saída (vendas_tratadas.csv)

| id_venda | data       | produto  | quantidade | preco_unitario | faturamento |
| -------- | ---------- | -------- | ---------- | -------------- | ----------- |
| 1        | 2024-05-01 | Notebook | 2          | 3500           | 7000        |
| 3        | 2024-06-01 | Teclado  | 1          | 150            | 150         |
| 5        | 2024-07-01 | Cadeira  | 3          | 800            | 2400        |


---

## Exemplo de Output no Terminal

=== Dados Extraídos ===
   id_venda        data   produto  quantidade  preco_unitario
0         1  2024/01/05  Notebook           2            3500
1         2  05-01-2024     Mouse           0              50
2         3  2024-01-06   Teclado           1             150
3         4  06/01/2024   Monitor          -1            1200
4         5  2024.01.07   Cadeira           3             800

2 vendas removidas por quantidade inválida

=== Dados Transformados ===
   id_venda        data   produto  quantidade  preco_unitario  faturamento
0         1  2024-05-01  Notebook           2            3500         7000
2         3  2024-06-01   Teclado           1             150          150
4         5  2024-07-01   Cadeira           3             800         2400

Faturamento total: R$ 9550

Faturamento por produto:
produto
Cadeira     2400
Notebook    7000
Teclado      150
Name: faturamento, dtype: int64

Arquivo salvo em: data/processed/vendas_tratadas.csv
