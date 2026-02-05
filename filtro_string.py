import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from extrair_performance import medir_performance, salvar_resultado

# ================= PANDAS =================
def filtrar_string_participantes_pandas(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
    return df[df["SG_UF_PROVA"] == "PE"]

def filtrar_string_resultados_pandas(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
    return df[df["SG_UF_PROVA"] == "PE"]

# ================= SPARK =================
def criar_sessao():
    return (
        SparkSession.builder
        .appName("Comparativo Pandas vs Spark")
        .master("local[*]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )

def filtrar_string_participantes_spark(caminho_csv):
    spark = criar_sessao()

    df = (
        spark.read
        .option("header", True)
        .option("sep", ";")
        .option("encoding", "iso-8859-1")
        .csv(caminho_csv)
    )

    return df.filter(col("SG_UF_PROVA") == "PE"), spark


def filtrar_string_resultados_spark(caminho_csv):
    spark = criar_sessao()

    df = (
        spark.read
        .option("header", True)
        .option("sep", ";")
        .option("encoding", "iso-8859-1")
        .csv(caminho_csv)
    )

    return df.filter(col("SG_UF_PROVA") == "PE"), spark


# ================= MAIN =================
if __name__ == "__main__":

    testes = [
        ("Dados_ENEM/PARTICIPANTES_2024.csv", filtrar_string_participantes_pandas, "pandas"),
        ("Dados_ENEM/RESULTADOS_2024.csv", filtrar_string_resultados_pandas, "pandas"),
        ("Dados_ENEM/PARTICIPANTES_2024.csv", filtrar_string_participantes_spark, "spark"),
        ("Dados_ENEM/RESULTADOS_2024.csv", filtrar_string_resultados_spark, "spark"),
    ]

    for arquivo, func, tipo in testes:
        stats = medir_performance(func, arquivo)
        salvar_resultado("Resultados/filtro_string.csv", arquivo, tipo, stats)

    print("\nBenchmark finalizado. Resultados salvos.")