from code_import.executor import executar_benchmark

def groupby_pandas(df):

    resumo = df.groupby(
        'residencia_provincia_nombre'
    ).agg({
        'id_evento_caso': 'count',
        'edad': ['min', 'max', 'mean']
    })

    resumo.columns = [
        'contagem_casos',
        'idade_minima',
        'idade_maxima',
        'idade_media'
    ]

    resumo = resumo.reset_index()

    return resumo


def groupby_spark(df):

    from pyspark.sql.functions import (
        count,
        min,
        max,
        avg
    )

    resumo = df.groupBy(
        'residencia_provincia_nombre'
    ).agg(
        count('id_evento_caso').alias(
            'contagem_casos'
        ),

        min('edad').alias(
            'idade_minima'
        ),

        max('edad').alias(
            'idade_maxima'
        ),

        avg('edad').alias(
            'idade_media'
        )
    )

    resumo.count()

    return resumo

executar_benchmark(
    nome_arquivo_teste="groupby",
    funcao_pandas=groupby_pandas,
    funcao_spark=groupby_spark
)
