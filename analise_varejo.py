import pandas as pd
from pathlib import Path

# Diretório do projeto
BASE_DIR = Path(__file__).resolve().parent
caminho_csv = BASE_DIR / "data" / "base_varejo.csv"

df = pd.read_csv(caminho_csv, sep=";", na_values="#N/D")

# Remove as colunas vazias sem nome que vem no final do arquivo.
df = df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"], errors="ignore")

# Guardo o total de linhas antes da limpeza para comparar no final.
linhas_antes = len(df)



# limpeza 

# Padronizo o nome do produto em maiusculas
df["PR_NOME"] = df["PR_NOME"].str.upper()

# Removo linhas totalmente iguais
df = df.drop_duplicates()

# Marco a categoria ausente em vez de apagar a linha, para nao perder os dados do cliente.
df["PR_CAT"] = df["PR_CAT"].fillna("NAO INFORMADO")
