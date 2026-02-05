import time
import psutil
import os
import pandas as pd

def medir_performance(func, *args):
    processo = psutil.Process()

    mem_antes = processo.memory_info().rss / (1024 ** 2)
    cpu_antes = time.process_time()
    inicio = time.time()

    resultado = func(*args)

    spark = None
    if isinstance(resultado, tuple):
        resultado, spark = resultado

    if "pyspark" in str(type(resultado)):
        linhas = resultado.count()
    else:
        linhas = len(resultado)

    if spark:
        spark.stop()

    fim = time.time()
    cpu_depois = time.process_time()
    mem_depois = processo.memory_info().rss / (1024 ** 2)

    tempo_total = round(fim - inicio, 2)
    tempo_cpu = round(cpu_depois - cpu_antes, 2)
    uso_memoria = round(mem_depois - mem_antes, 2)
    linhas_segundo = round(linhas / tempo_total, 2) if tempo_total > 0 else 0

    return {
        "linhas_processadas": linhas,
        "tempo_total_s": tempo_total,
        "tempo_cpu_s": tempo_cpu,
        "memoria_MB": uso_memoria,
        "linhas_por_segundo": linhas_segundo,
    }


def salvar_resultado(arquivo_saida, arquivo, execucao, stats):
    linha = {
        "Arquivo": os.path.basename(arquivo),
        "Execucao": execucao,
        **stats
    }

    df_linha = pd.DataFrame([linha])

    if os.path.exists(arquivo_saida):
        df_linha.to_csv(arquivo_saida, mode="a", header=False, index=False)
    else:
        df_linha.to_csv(arquivo_saida, mode="w", header=True, index=False)