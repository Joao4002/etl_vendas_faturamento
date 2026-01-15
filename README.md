# Projeto ETL de Vendas e Faturamento

##  Descrição
Este projeto foi desenvolvido para praticar conceitos de Engenharia de Dados, simulando um pipeline ETL simples a partir de um arquivo CSV de vendas.

O processo envolve a extração dos dados, aplicação de regras de negócio e o carregamento dos dados tratados em um banco SQL para análise de faturamento.

---

##  Tecnologias utilizadas
- Python
- Pandas
- SQL
- Git e GitHub

---

##  Regras de negócio aplicadas
- Remoção de vendas com quantidade menor ou igual a zero  
- Padronização do campo de data para o formato `YYYY-MM-DD`  
- Cálculo do faturamento com base na quantidade e no preço unitário  

---

##  Fluxo do pipeline
1. Leitura dos dados a partir de um arquivo CSV  
2. Tratamento e limpeza dos dados com Pandas  
3. Aplicação das regras de negócio  
4. Carga dos dados tratados em banco SQL  

---

## Estrutura do projeto

A estrutura foi organizada para separar dados, lógica de negócio e execução do pipeline.


etl_vendas_faturamento/
├── data/
│   ├── raw/
│   │   └── vendas.csv
│   └── processed/
│       └── vendas_tratadas.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
└── README.md


---


##  Como executar o projeto

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

2. Acesse a pasta do projeto:

cd etl_vendas_faturamento

3. Crie e ative um ambiente virtual (opcional):

python -m venv venv
venv\Scripts\activate

4. Instale as dependências:

pip install pandas

5. Execute o pipeline:

python main.py

Após a execução, os dados tratados serão salvos em arquivo CSV e carregados no banco SQL.


---

## Objetivo do projeto

O objetivo deste projeto foi fazer um processo de ELT completo do dado bruto até o armazenamento em um banco de dados, simulando exatamente o que é mais feito em processos de engenharia de dados por empresas não só brasileira como mundialmente.

## English version

This project was developed to practice Data Engineering concepts by simulating a simple ETL pipeline using a sales CSV file.

The process includes data extraction, business rule application, and loading the processed data into a SQL database for revenue analysis.

1. Clone the repository:

git clone https://github.com/your-username/your-repository.git

2. Acess the project folder:

cd etl_vendas_faturamento

3. Install dependencies:

pip install pandas


4. Run the pipeline:

python main.py 

## Project structure

The structure was organized to separate data, business logic, and pipeline execution.

etl_vendas_faturamento/
├── data/
│   ├── raw/
│   │   └── vendas.csv
│   └── processed/
│       └── vendas_tratadas.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
└── README.md


