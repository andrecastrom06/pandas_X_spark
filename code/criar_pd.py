import pandas as pd
import numpy as np

filas = 1000000 # Exemplo de volume de dados
columnas_list = ['col1', 'col2', 'col3', 'col4']

# Lógica do Anexo I
df_pd = pd.DataFrame(np.random.randint(0, 100, size=(filas, 4)), columns=columnas_list)
