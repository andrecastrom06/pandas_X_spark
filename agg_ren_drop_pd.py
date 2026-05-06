# Renomear
df_pd = df_pd.rename(columns={'sexo': 'genero'})

# Agregar (Nova coluna)
df_pd['nova_coluna'] = 0

# Eliminar
df_pd = df_pd.drop(columns=['col1'])
