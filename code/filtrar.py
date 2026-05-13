from code_import.executor import executar_benchmark

def filter_pandas(df):

    filtro_1 = df[
        df['edad'] > 30
    ]

    filtro_1.head()

    filtro_2 = df[
        (df['edad'] > 30) &
        (
            df['residencia_provincia_nombre']
            == 'Buenos Aires'
        )
    ]

    filtro_2.head()

    return filtro_2


def filter_spark(df):

    from pyspark.sql.functions import col

    filtro_1 = df.filter(
        col('edad') > 30
    )

    filtro_1.collect()

    filtro_2 = df.filter(
        (col('edad') > 30) &
        (
            col(
                'residencia_provincia_nombre'
            ) == 'Buenos Aires'
        )
    )

    filtro_2.collect()

    return filtro_2


executar_benchmark(
    nome_arquivo_teste="filter",
    funcao_pandas=filter_pandas,
    funcao_spark=filter_spark
)