from code_import.executor import executar_benchmark

def orderby_pandas(df):

    resultado = df.sort_values(
        by='edad',
        ascending=True
    )

    resultado.head()

    return resultado


def orderby_spark(df):

    from pyspark.sql.functions import col

    resultado = df.orderBy(
        col('edad').asc()
    )

    resultado.collect()

    return resultado

executar_benchmark(
    nome_arquivo_teste="orderby",
    funcao_pandas=orderby_pandas,
    funcao_spark=orderby_spark
)