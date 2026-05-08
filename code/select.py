from code_import.executor import executar_benchmark

def select_columns_pandas(df):

    resultado = df[
        [
            'id_evento_caso',
            'sexo',
            'edad',
            'residencia_provincia_nombre',
            'fallecido'
        ]
    ]

    resultado.head()

    return resultado

def select_columns_spark(df):

    resultado = df.select(
        'id_evento_caso',
        'sexo',
        'edad',
        'residencia_provincia_nombre',
        'fallecido'
    )

    resultado.collect()

    return resultado

executar_benchmark(
    nome_arquivo_teste="select_columns",
    funcao_pandas=select_columns_pandas,
    funcao_spark=select_columns_spark
)