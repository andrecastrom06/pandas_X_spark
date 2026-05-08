import pandas as pd
import os

# Supondo que df_pandas seja o seu DataFrame carregado
path_output = os.path.join('data', 'nome.csv')

# Lógica do artigo: salvar sem o índice do pandas
df_pandas.to_csv(path_output, sep=',', header=True, index=False)

print(f"Arquivo salvo com sucesso em: {path_output}")
