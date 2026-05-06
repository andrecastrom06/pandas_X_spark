# Filtro simples
df_filtro_ps = df_ps.filter(df_ps.clasificacion_resumen == 'Confirmado')

# Distinct
df_distinct_ps = df_ps.distinct()
