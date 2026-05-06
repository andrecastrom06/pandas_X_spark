from pyspark.sql import functions as F

# Lógica de agregação do Spark (usando alias para renomear na hora)
resumo_ps = df_casos.groupBy('residencia_provincia_nombre').agg(
    F.count('id_evento_caso').alias('contagem'),
    F.min('edad').alias('idade_min'),
    F.max('edad').alias('idade_max'),
    F.avg('edad').alias('idade_avg')
)
