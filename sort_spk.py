from pyspark.sql.functions import col

# Lógica do Anexo III do artigo
df_ps = df_ps.orderBy(col("id_evento_caso").asc())
