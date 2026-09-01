import pandas as pd
from pyspark.sql import SparkSession

from code_import.metricas import (
    capturar_metricas_inicio,
    capturar_metricas_fim,
    medir_tempo
)

from code_import.result import (
    exportar_metricas,
    exportar_inicializacao_spark
)


def _criar_spark():
    fim = medir_tempo()

    sessao = SparkSession.builder \
        .master("local[*]") \
        .appName("Benchmark") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    return sessao, fim()


spark, TEMPO_INICIALIZACAO_SPARK = _criar_spark()


DATASETS = [
    "covid_2020_2021_200.csv",
    "covid_2020_2021_600.csv",
    "covid_2020_2021_1800.csv",
    "Covid19Casos.csv"
]

NUM_EXECUCOES = 5


def _ler_csv_spark(dataset):
    fim_leitura = medir_tempo()

    df_spark = spark.read.csv(
        f"../data/{dataset}",
        header=True,
        inferSchema=True
    )
    df_spark.cache()
    df_spark.count()

    return df_spark, fim_leitura()


def executar_benchmark(
    nome_arquivo_teste,
    funcao_pandas,
    funcao_spark
):

    exportar_inicializacao_spark(
        nome_arquivo=nome_arquivo_teste,
        tempo_inicializacao=TEMPO_INICIALIZACAO_SPARK
    )

    for dataset in DATASETS:

        for execucao in range(1, NUM_EXECUCOES + 1):

            fim_leitura = medir_tempo()
            df = pd.read_csv(f"../data/{dataset}")
            tempo_leitura_csv = fim_leitura()

            inicio = capturar_metricas_inicio()

            funcao_pandas(df)

            metricas = capturar_metricas_fim(inicio)
            metricas['tempo_leitura_csv'] = tempo_leitura_csv
            metricas['tempo_total'] = round(
                tempo_leitura_csv + metricas['tempo_resposta'],
                4
            )

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

        for execucao in range(1, NUM_EXECUCOES + 1):

            df_spark, tempo_leitura_csv = _ler_csv_spark(dataset)

            inicio = capturar_metricas_inicio()

            funcao_spark(df_spark)

            metricas = capturar_metricas_fim(inicio)
            metricas['tempo_leitura_csv'] = tempo_leitura_csv
            metricas['tempo_inicializacao_spark'] = (
                TEMPO_INICIALIZACAO_SPARK
            )
            metricas['tempo_total'] = round(
                TEMPO_INICIALIZACAO_SPARK
                + tempo_leitura_csv
                + metricas['tempo_resposta'],
                4
            )

            df_spark.unpersist()

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