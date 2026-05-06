# Conversão para datetime
df_pd['fecha_internacion'] = pd.to_datetime(df_pd['fecha_internacion'], format='%Y-%m-%d')
