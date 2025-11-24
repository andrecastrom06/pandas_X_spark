import pandas as pd
import time
import psutil
import os

def bytes_para_mb(b):
    return round(b / 1024 / 1024, 2)

processo = psutil.Process(os.getpid())

t0_total = time.time()
cpu_inicio = processo.cpu_times()
mem_inicio = processo.memory_info().rss

t0_latency = time.time()

res = pd.read_csv("RESULTADOS_2024.csv", sep=";", encoding="latin1")

t1_latency = time.time()
latencia = t1_latency - t0_latency

filtrado = res[res["NU_NOTA_MT"] >= 900]

agrupado = (
    filtrado
    .groupby("SG_UF_PROVA")["NU_NOTA_REDACAO"]
    .mean()
    .sort_values(ascending=False)
)

print("\nResultado Pandas:")
print(agrupado)

t1_total = time.time()
cpu_fim = processo.cpu_times()
mem_fim = processo.memory_info().rss

tempo_total = t1_total - t0_total
cpu_user = cpu_fim.user - cpu_inicio.user
memoria_usada = bytes_para_mb(mem_fim - mem_inicio)

print("\n===== MÉTRICAS PANDAS =====")
print(f"Tempo de CPU: {cpu_user:.4f} segundos")
print(f"Tempo total: {tempo_total:.4f} segundos")
print(f"Latência leitura: {latencia:.4f} segundos")
print(f"Memória consumida: {memoria_usada} MB")