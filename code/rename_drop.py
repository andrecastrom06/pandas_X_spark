from code_import.executor import executar_benchmark


def rename_drop_pandas(df):

    df_rename = df.rename(columns={
        'id_evento_caso': 'id_caso',
        'sexo': 'genero',
        'edad': 'idade',
        'fallecido': 'obito'
    })

    df_drop = df_rename.drop(columns=[
        'fecha_fallecimiento',
        'cuidado_intensivo',
        'asistencia_respiratoria_mecanica'
    ])

    df_drop.head()

    return df_drop


def rename_drop_spark(df):

    df = df.withColumnRenamed(
        'id_evento_caso',
        'id_caso'
    )

    df = df.withColumnRenamed(
        'sexo',
        'genero'
    )

    df = df.withColumnRenamed(
        'edad',
        'idade'
    )

    df = df.withColumnRenamed(
        'fallecido',
        'obito'
    )

    df = df.drop(
        'fecha_fallecimiento',
        'cuidado_intensivo',
        'asistencia_respiratoria_mecanica'
    )

    df.collect()

    return df


executar_benchmark(
    nome_arquivo_teste="rename_drop",
    funcao_pandas=rename_drop_pandas,
    funcao_spark=rename_drop_spark
)