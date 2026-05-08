from pyspark.sql import SparkSession
import os

# Inicializa a sessão Spark
spark = SparkSession.builder.appName("LeituraArtigo").getOrCreate()

# Caminho para o arquivo
path = os.path.join('data', 'nome.csv')

# Lógica do artigo: leitura com inferência de schema e cabeçalho
df_spark = spark.read.option("header", True) \
    .option("sep", ",") \
    .option("inferSchema", "true") \
    .csv(path)

print(f"Spark leu {df_spark.count()} linhas.")
