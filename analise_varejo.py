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


# Tira os espacos das pontas do texto de uma coluna.
def tirar_espacos(dados, coluna):
    dados[coluna] = dados[coluna].str.strip()
    return dados

# Retorna a media de uma coluna numerica.
def calcular_media(dados, coluna):
    media = dados[coluna].mean()
    return media

df = tirar_espacos(df, "PR_CAT")

media_filhos = calcular_media(df, "CL_FHL")

# estatisticas ---

contagem = df["CL_FHL"].count()
media = df["CL_FHL"].mean()
minimo = df["CL_FHL"].min()
maximo = df["CL_FHL"].max()

print("Validos:", contagem)
print("Media:", media)
print("Minimo:", minimo)
print("Maximo:", maximo)


# filtro e agrupamentos 

# Filtro: so os itens da categoria ALIMENTOS 
df_alimentos = df[df["PR_CAT"] == "ALIMENTOS"]


# Quantos itens aparecem em cada categoria.
print(df.groupby("PR_CAT")["PR_ID"].count())

# Quantos itens por genero do cliente 
print(df.groupby("CL_GENERO")["PR_ID"].count())

# exportacao 

df.to_csv(BASE_DIR / "varejo_limpo.csv", index=False)
linhas_depois = len(df)
