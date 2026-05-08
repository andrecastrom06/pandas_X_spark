from code_import.executor import executar_benchmark

def count_rows_pandas(df):

    quantidade_linhas = len(df)

    print(
        f"PANDAS -> Quantidade de linhas: "
        f"{quantidade_linhas}"
    )

    return quantidade_linhas


def count_rows_spark(df):

    quantidade_linhas = df.count()

    print(
        f"SPARK -> Quantidade de linhas: "
        f"{quantidade_linhas}"
    )

    return quantidade_linhas


executar_benchmark(
    nome_arquivo_teste="count_rows",
    funcao_pandas=count_rows_pandas,
    funcao_spark=count_rows_spark
)