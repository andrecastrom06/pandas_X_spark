from pyspark.sql.functions import col

# No Spark, utiliza-se o método .select()
columnas = ['id_evento_caso', 'sexo', 'edad']
df_select_ps = df_ps.select(*columnas)
