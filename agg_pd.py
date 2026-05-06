# Lógica de agregação múltipla do Pandas
resumo_pd = df_casos.groupby('residencia_provincia_nombre').agg({
    'id_evento_caso': 'count',
    'edad': ['min', 'max', 'mean'] # mean equivale ao AVG
})

# Renomeando colunas resultantes para facilitar
resumo_pd.columns = ['contagem', 'idade_min', 'idade_max', 'idade_avg']
