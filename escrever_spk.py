import os

# Supondo que df_spark seja o seu DataFrame Spark
path_output = os.path.join('data', 'nome')

# Lógica do artigo: usar overwrite para não dar erro se a pasta já existir
# Nota: O Spark salvará uma PASTA com arquivos particionados dentro
df_spark.write.mode('overwrite') \
    .option("header", "true") \
    .csv(path_output)

print(f"Pasta de resultados criada em: {path_output}")
