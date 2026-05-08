from code_import.executor import executar_benchmark

def groupby_pandas(df):

    resumo = df.groupby(
        'residencia_provincia_nombre'
    ).size().reset_index(
        name='quantidade_casos'
    )

    resumo.head()

    return resumo


def groupby_spark(df):

    from pyspark.sql.functions import count

    resumo = df.groupBy(
        'residencia_provincia_nombre'
    ).agg(
        count('*').alias(
            'quantidade_casos'
        )
    )

    resumo.collect()

    return resumo


executar_benchmark(
    nome_arquivo_teste="groupby_provincia",
    funcao_pandas=groupby_pandas,
    funcao_spark=groupby_spark
)