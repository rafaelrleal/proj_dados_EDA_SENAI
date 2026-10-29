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
