from code_import.executor import executar_benchmark


def cast_pandas(df):

    df['edad'] = df['edad'].astype('float')

    df['fecha_diagnostico'] = (
        df['fecha_diagnostico']
        .astype('datetime64[ns]')
    )

    df['id_evento_caso'] = (
        df['id_evento_caso']
        .astype('string')
    )

    df['fallecido'] = (
        df['fallecido']
        .astype('string')
    )

    df.info()

    return df


def cast_spark(df):

    from pyspark.sql.functions import col

    from pyspark.sql.types import (
        FloatType,
        DateType,
        StringType
    )

    df = df.withColumn(
        'edad',
        col('edad').cast(FloatType())
    )

    df = df.withColumn(
        'fecha_diagnostico',
        col('fecha_diagnostico').cast(DateType())
    )

    df = df.withColumn(
        'id_evento_caso',
        col('id_evento_caso').cast(StringType())
    )

    df = df.withColumn(
        'fallecido',
        col('fallecido').cast(StringType())
    )

    df.collect()

    return df


executar_benchmark(
    nome_arquivo_teste="cast",
    funcao_pandas=cast_pandas,
    funcao_spark=cast_spark
)