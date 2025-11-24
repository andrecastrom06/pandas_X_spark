from pyspark.sql import SparkSession
import time
import psutil
import os

def bytes_para_mb(b):
    return round(b / 1024 / 1024, 2)

processo = psutil.Process(os.getpid())

spark = (
    SparkSession.builder
    .appName("Pandas X Spark")
    .master("local[*]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "0.0.0.0")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)

print("\nSpark session criada com sucesso!\n")

tempo_inicio = time.time()
cpu_inicio = processo.cpu_times()
mem_inicio = processo.memory_info().rss  

t0_latency = time.time()  

res = spark.read.csv(
    'RESULTADOS_2024.csv',
    header=True,
    inferSchema=True,
    sep=";"
)

t1_latency = time.time()  

latencia = t1_latency - t0_latency

linhas_res = res.count()
media_nota_redacao = res.selectExpr("avg(NU_NOTA_REDACAO)").first()[0]

tempo_fim = time.time()
cpu_fim = processo.cpu_times()
mem_fim = processo.memory_info().rss

tempo_total = tempo_fim - tempo_inicio
cpu_user = cpu_fim.user - cpu_inicio.user
memoria_usada = bytes_para_mb(mem_fim - mem_inicio)

print("Linhas resultados:", linhas_res)
print("Média nota redação:", media_nota_redacao)
print("\n===== MÉTRICAS =====")
print(f"Latência (início até leitura): {latencia:.4f} segundos")
print(f"Tempo de execução total: {tempo_total:.4f} segundos")
print(f"Tempo de CPU: {cpu_user:.4f} segundos")
print(f"Memória consumida: {memoria_usada} MB")

spark.stop()