from code_import.executor import executar_benchmark


def create_drop_pandas(df):

    novo_df = df[
        [
            'id_evento_caso',
            'edad'
        ]
    ].copy()

    del novo_df

    return df


def create_drop_spark(df):

    novo_df = df.select(
        'id_evento_caso',
        'edad'
    )

    novo_df.count()

    del novo_df

    return df


executar_benchmark(
    nome_arquivo_teste="create_drop",
    funcao_pandas=create_drop_pandas,
    funcao_spark=create_drop_spark
)