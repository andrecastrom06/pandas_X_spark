from code_import.executor import executar_benchmark


def cast_pandas(df):

    df['edad'] = df['edad'].astype('float')

    df['id_evento_caso'] = (
        df['id_evento_caso']
        .astype('string')
    )

    df['residencia_provincia_nombre'] = (
        df['residencia_provincia_nombre']
        .astype('string')
    )

    df.info()

    return df


def cast_spark(df):

    from pyspark.sql.functions import col

    from pyspark.sql.types import (
        FloatType,
        StringType
    )

    df = df.withColumn(
        'edad',
        col('edad').cast(FloatType())
    )

    df = df.withColumn(
        'id_evento_caso',
        col('id_evento_caso').cast(StringType())
    )

    df = df.withColumn(
        'residencia_provincia_nombre',
        col('residencia_provincia_nombre').cast(StringType())
    )

    df.printSchema()

    return df


executar_benchmark(
    nome_arquivo_teste="cast",
    funcao_pandas=cast_pandas,
    funcao_spark=cast_spark
)