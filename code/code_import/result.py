def exportar_metricas(
    nome_arquivo,
    ferramenta,
    dataset,
    execucao,
    metricas
):
    arquivo_saida = f"../result_local/{nome_arquivo}.txt"

    with open(arquivo_saida, 'a', encoding='utf-8') as f:

        f.write(
            f"\n{'=' * 60}\n"
        )

        f.write(
            f"Ferramenta: {ferramenta}\n"
        )

        f.write(
            f"Dataset: {dataset}\n"
        )

        f.write(
            f"Execução: {execucao}\n"
        )

        f.write(
            f"{'-' * 60}\n"
        )

        if 'tempo_leitura_csv' in metricas:
            f.write(
                f"Tempo de Leitura CSV: "
                f"{metricas['tempo_leitura_csv']} s\n"
            )

        if 'tempo_inicializacao_spark' in metricas:
            f.write(
                f"Tempo de Inicialização Spark: "
                f"{metricas['tempo_inicializacao_spark']} s\n"
            )

        f.write(
            f"Tempo de Resposta: "
            f"{metricas['tempo_resposta']} s\n"
        )

        if 'tempo_total' in metricas:
            f.write(
                f"Tempo Total: "
                f"{metricas['tempo_total']} s\n"
            )

        f.write(
            f"Tempo de CPU: "
            f"{metricas['tempo_cpu']} s\n"
        )

        f.write(
            f"Uso de Memória: "
            f"{metricas['memoria_pico']} MB\n"
        )


def exportar_inicializacao_spark(
    nome_arquivo,
    tempo_inicializacao
):
    arquivo_saida = f"../result_local/{nome_arquivo}.txt"

    with open(arquivo_saida, 'a', encoding='utf-8') as f:
        f.write(f"\n{'=' * 60}\n")
        f.write("Fase: Inicialização do Spark\n")
        f.write(f"{'-' * 60}\n")
        f.write(
            f"Tempo de Inicialização Spark: "
            f"{tempo_inicializacao} s\n"
        )