import pandas as pd
from pyspark.sql import SparkSession

from code_import.metricas import (
    capturar_metricas_inicio,
    capturar_metricas_fim
)

from code_import.result import exportar_metricas


spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Benchmark") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()


DATASETS = [
    "covid_2020_2021_200.csv",
    "covid_2020_2021_600.csv",
    "covid_2020_2021_1800.csv"
]


def executar_benchmark(
    nome_arquivo_teste,
    funcao_pandas,
    funcao_spark
):


    for dataset in DATASETS:

        for execucao in range(1, 4):

            df = pd.read_csv(f"../data/{dataset}")

            inicio = capturar_metricas_inicio()

            funcao_pandas(df)

            metricas = capturar_metricas_fim(inicio)

            exportar_metricas(
                nome_arquivo=nome_arquivo_teste,
                ferramenta="Pandas",
                dataset=dataset,
                execucao=execucao,
                metricas=metricas
            )

            print(
                f"[PANDAS] "
                f"{dataset} "
                f"Execução {execucao} concluída"
            )


    for dataset in DATASETS:

        for execucao in range(1, 4):

            df_spark = spark.read.csv(
                f"../data/{dataset}",
                header=True,
                inferSchema=True
            )

            inicio = capturar_metricas_inicio()

            funcao_spark(df_spark)

            metricas = capturar_metricas_fim(inicio)

            exportar_metricas(
                nome_arquivo=nome_arquivo_teste,
                ferramenta="Spark",
                dataset=dataset,
                execucao=execucao,
                metricas=metricas
            )

            print(
                f"[SPARK] "
                f"{dataset} "
                f"Execução {execucao} concluída"
            )

    spark.stop()