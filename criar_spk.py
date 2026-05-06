from pyspark.sql import SparkSession
from pyspark.mllib.random import RandomRDDs

spark = SparkSession.builder.appName("CriacaoDF").getOrCreate()

# Lógica do Anexo I
df_ps = RandomRDDs.uniformVectorRDD(spark, filas, 4).map(lambda a : a.tolist()).toDF(columnas_list)
