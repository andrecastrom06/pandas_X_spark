from code_import.executor import executar_benchmark

def rename_drop_pandas(df):
    df_rename = df.rename(columns={
        "edad": "idade",
        "sexo": "genero",
        "fecha_apertura": "data_abertura"
    })

    df_drop = df_rename.drop(
        columns=[
            "fecha_fallecimiento",
            "cuidado_intensivo",
            "asistencia_respiratoria_mecanica"
        ],
        errors="ignore" 
    )

    return df_drop

def rename_drop_spark(df_spark):
    df_rename = (
        df_spark
        .withColumnRenamed("edad", "idade")
        .withColumnRenamed("sexo", "genero")
        .withColumnRenamed("fecha_apertura", "data_abertura")
    )

    df_drop = df_rename.drop(
        "fecha_fallecimiento",
        "cuidado_intensivo",
        "asistencia_respiratoria_mecanica"
    )

    df_drop.count()

    return df_drop

executar_benchmark(
    nome_arquivo_teste="rename_drop",
    funcao_pandas=rename_drop_pandas,
    funcao_spark=rename_drop_spark
)