from code_import.executor import executar_benchmark


def insert_drop_row_pandas(df):

    nova_linha = {
        'id_evento_caso': '999999',
        'edad': 30
    }

    temp_df = df[
        [
            'id_evento_caso',
            'edad'
        ]
    ].copy()

    temp_df.loc[len(temp_df)] = nova_linha

    temp_df = temp_df.drop(
        temp_df.index[-1]
    )

    temp_df.head()

    return temp_df


def insert_drop_row_spark(df):

    from pyspark.sql import Row

    spark = df.sparkSession

    temp_df = df.select(
        'id_evento_caso',
        'edad'
    )

    nova_linha = spark.createDataFrame([
        Row(
            id_evento_caso='999999',
            edad=30
        )
    ])

    temp_df = temp_df.union(nova_linha)

    temp_df.count()

    temp_df = temp_df.filter(
        temp_df.id_evento_caso != '999999'
    )

    temp_df.count()

    return temp_df


executar_benchmark(
    nome_arquivo_teste="insert_drop_row",
    funcao_pandas=insert_drop_row_pandas,
    funcao_spark=insert_drop_row_spark
)