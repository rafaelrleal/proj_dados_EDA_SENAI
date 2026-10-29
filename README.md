# Mini-Projeto Avaliativo - Analise Exploratouria de Dados (Varejo)

**Aluno:** Rafael Leal
**Turma:** T8

## Objetivo

Realizar uma Analise  (AED) sobre uma base de varejo,
transformando os dados brutos em informações  sobre o negócio:
avaliar qualidade, limpeza justificada, estatísticas, filtros e
agrupamentos, e exportação.

## Origem dos dados

- Dados = [Base Varejo - Kaggle](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)`.



## Significado das colunas utilizadas



| Coluna    | Significado                          |
| ----------- | -------------------------------------- |
| DATA      | Data da compra                       |
| CO_ID     | Identificador da compra              |
| CL_ID     | Identificador do cliente             |
| CL_GENERO | Gênero do cliente (F/M)             |
| CL_EC     | Estado civil do cliente (código)    |
| CL_FHL    | Número de filhos do cliente (0 a 4) |
| CL_SEG    | Segmento do cliente (A/B/C)          |
| PR_ID     | Identificador do produto             |
| PR_CAT    | Categoria do produto                 |
| PR_NOME   | Nome do produto                      |


## Decisões de limpeza

- **Colunas vazias:** o arquivo traz 4 colunas sem nome no final, que foram removidas.
- **Padronização de texto:** `PR_NOME` foi convertido para maiúsculas para
  evitar nomes repetidos apenas por diferença de caixa.
- **Categoria ausente:** os registros com categoria ausente  foram
  marcados como `NAO INFORMADO` .
- **Duplicatas:** foram removidas as linhas idênticas em todas as colunas
  (96.553 linhas).


## Conclusões

- A base tem 830.000 registros antes da limpeza e 733.447 depois; foram
  removidas 96.553 linhas duplicadas.
- Os dados cobrem 1.000 clientes, 18.471 compras e 229 produtos, no
  período de 01/01/2020 a 31/10/2021.
- ALIMENTOS é de longe a maior categoria (384.197 itens), seguida por
  HIGIENE (137.702) e LIMPEZA (128.632).
- A distribuição por gênero é equilibrada: F = 382.427  e
  M = 351.020 .
- A média de filhos por item de compra é 1,15 (mínimo 0, máximo 4),
  indicando um público predominantemente de famílias pequenas.

## Oque foi usado

Python 3.12 e pandas. este projeto usa `uv` pra gerir ambientes
