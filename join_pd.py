import pandas as pd
import os

# Carregando os dois datasets
df_casos = pd.read_csv('data/200mb.csv')
df_provincias = pd.read_csv('data/provincias.csv')

# Lógica do artigo: merge (join) baseado nos nomes das províncias
df_join_pd = pd.merge(
    df_casos, 
    df_provincias, 
    left_on='residencia_provincia_nombre', 
    right_on='iso_nombre',
    how='inner'
)
