from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinArtigo").getOrCreate()

df_casos = spark.read.option("header", True).csv('data/200mb.csv')
df_provincias = spark.read.option("header", True).csv('data/provincias.csv')

# Lógica do artigo: join explícito definindo as colunas correspondentes
df_join_ps = df_casos.join(
    df_provincias, 
    df_casos.residencia_provincia_nombre == df_provincias.iso_nombre, 
    how='inner'
)
