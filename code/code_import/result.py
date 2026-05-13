def exportar_metricas(
    nome_arquivo,
    ferramenta,
    dataset,
    execucao,
    metricas
):
    arquivo_saida = f"../result/{nome_arquivo}.txt"

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

        f.write(
            f"Tempo de Resposta: "
            f"{metricas['tempo_resposta']} s\n"
        )

        f.write(
            f"Tempo de CPU: "
            f"{metricas['tempo_cpu']} s\n"
        )

        f.write(
            f"Uso de Memória: "
            f"{metricas['memoria_pico']} MB\n"
        )