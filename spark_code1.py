from pyspark.sql import SparkSession
import time
import psutil
import os

def bytes_para_mb(b):
    return round(b / 1024 / 1024, 2)

processo = psutil.Process(os.getpid())

spark = (
    SparkSession.builder
    .appName("Comparativo Pandas vs Spark")
    .master("local[*]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "0.0.0.0")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)

t0_total = time.time()
cpu_inicio = processo.cpu_times()
mem_inicio = processo.memory_info().rss

t0_latency = time.time()

res = spark.read.csv("RESULTADOS_2024.csv", header=True, sep=";", inferSchema=True)

t1_latency = time.time()
latencia = t1_latency - t0_latency

filtrado = res.filter(res["NU_NOTA_MT"] >= 900)

agrupado = (
    filtrado.groupBy("SG_UF_PROVA")
    .avg("NU_NOTA_REDACAO")
    .orderBy("avg(NU_NOTA_REDACAO)", ascending=False)
)

print("\nResultado Spark:")
agrupado.show(truncate=False)

t1_total = time.time()
cpu_fim = processo.cpu_times()
mem_fim = processo.memory_info().rss

tempo_total = t1_total - t0_total
cpu_user = cpu_fim.user - cpu_inicio.user
memoria_usada = bytes_para_mb(mem_fim - mem_inicio)

print("\n===== MÉTRICAS SPARK =====")
print(f"Tempo de CPU: {cpu_user:.4f} segundos")
print(f"Tempo total: {tempo_total:.4f} segundos")
print(f"Latência leitura: {latencia:.4f} segundos")
print(f"Memória consumida: {memoria_usada} MB")

spark.stop()