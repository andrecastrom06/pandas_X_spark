from code_import.executor import executar_benchmark

def join_pandas(df):

    tabela_idade = df[
        [
            'id_evento_caso',
            'edad'
        ]
    ].copy()

    tabela_provincia = df[
        [
            'id_evento_caso',
            'residencia_provincia_nombre'
        ]
    ].copy()

    resultado = tabela_idade.merge(
        tabela_provincia,
        on='id_evento_caso',
        how='inner'
    )

    resultado.head()

    return resultado


def join_spark(df):
    tabela_idade = df.select(
        'id_evento_caso',
        'edad'
    )

    tabela_provincia = df.select(
        'id_evento_caso',
        'residencia_provincia_nombre'
    )

    resultado = tabela_idade.join(
        tabela_provincia,
        on='id_evento_caso',
        how='inner'
    )

    resultado.collect()

    return resultado


executar_benchmark(
    nome_arquivo_teste="join",
    funcao_pandas=join_pandas,
    funcao_spark=join_spark
)