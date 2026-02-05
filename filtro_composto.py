import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from extrair_performance import medir_performance, salvar_resultado

# ================= PANDAS =================
def filtrar_composto_participantes_pandas(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
    df["TP_FAIXA_ETARIA"] = pd.to_numeric(df["TP_FAIXA_ETARIA"], errors="coerce")
    return df[(df["TP_FAIXA_ETARIA"] > 15) & (df["TP_FAIXA_ETARIA"] <= 20)]

def filtrar_composto_resultados_pandas(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
    df["NU_NOTA_REDACAO"] = pd.to_numeric(df["NU_NOTA_REDACAO"], errors="coerce")
    return df[(df["NU_NOTA_REDACAO"] > 800) & (df["NU_NOTA_REDACAO"] <= 900)]

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

def filtrar_composto_participantes_spark(caminho_csv):
    spark = criar_sessao()

    df = (
        spark.read
        .option("header", True)
        .option("sep", ";")
        .option("encoding", "iso-8859-1")
        .csv(caminho_csv)
    )

    df = df.withColumn("TP_FAIXA_ETARIA", col("TP_FAIXA_ETARIA").cast("int"))
    return df.filter((col("TP_FAIXA_ETARIA") > 15) & (col("TP_FAIXA_ETARIA") <= 20)), spark


def filtrar_composto_resultados_spark(caminho_csv):
    spark = criar_sessao()

    df = (
        spark.read
        .option("header", True)
        .option("sep", ";")
        .option("encoding", "iso-8859-1")
        .csv(caminho_csv)
    )

    df = df.withColumn("NU_NOTA_REDACAO", col("NU_NOTA_REDACAO").cast("int"))
    return df.filter((col("NU_NOTA_REDACAO") > 800) & (col("NU_NOTA_REDACAO") <= 900)), spark


# ================= MAIN =================
if __name__ == "__main__":

    testes = [
        ("Dados_ENEM/PARTICIPANTES_2024.csv", filtrar_composto_participantes_pandas, "pandas"),
        ("Dados_ENEM/RESULTADOS_2024.csv", filtrar_composto_resultados_pandas, "pandas"),
        ("Dados_ENEM/PARTICIPANTES_2024.csv", filtrar_composto_participantes_spark, "spark"),
        ("Dados_ENEM/RESULTADOS_2024.csv", filtrar_composto_resultados_spark, "spark"),
    ]

    for arquivo, func, tipo in testes:
        stats = medir_performance(func, arquivo)
        salvar_resultado("Resultados/filtro_composto.csv", arquivo, tipo, stats)

    print("\nBenchmark finalizado. Resultados salvos.")