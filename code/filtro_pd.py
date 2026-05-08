# Filtro simples (Exemplo: apenas confirmados)
df_filtro_pd = df_pd[df_pd['clasificacion_resumen'] == 'Confirmado']

# Distinct (Filas únicas)
df_distinct_pd = df_pd.drop_duplicates()
