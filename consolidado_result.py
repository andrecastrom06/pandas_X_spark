import re
import os
import pandas as pd

pastas = ["local", "distribuidos"]

for pasta in pastas:

    PASTA_RESULTADOS = f"./result_{pasta}"

    ARQUIVO_SAIDA = (
        f"./result_{pasta}/"
        f"benchmark_consolidado_{pasta}.csv"
    )

    dados = []

    if not os.path.exists(PASTA_RESULTADOS):

        print(
            f"Pasta não encontrada: "
            f"{PASTA_RESULTADOS}"
        )

        continue

    arquivos_txt = [
        os.path.join(PASTA_RESULTADOS, arq)
        for arq in os.listdir(PASTA_RESULTADOS)
        if arq.endswith(".txt")
    ]

    for arquivo in arquivos_txt:

        print(f"Lendo: {arquivo}")

        # pega nome do arquivo sem .txt
        transformacao = os.path.splitext(
            os.path.basename(arquivo)
        )[0]

        with open(
            arquivo,
            "r",
            encoding="utf-8"
        ) as f:

            conteudo = f.read()

        blocos = re.split(
            r"=+",
            conteudo
        )

        for bloco in blocos:

            bloco = bloco.strip()

            if not bloco:
                continue

            try:

                ferramenta = re.search(
                    r"Ferramenta:\s*(.*)",
                    bloco
                ).group(1).strip()

                dataset = re.search(
                    r"Dataset:\s*(.*)",
                    bloco
                ).group(1).strip()

                execucao = re.search(
                    r"Execução:\s*(.*)",
                    bloco
                ).group(1).strip()

                tempo_resposta = re.search(
                    r"Tempo de Resposta:\s*(.*)",
                    bloco
                ).group(1).strip()

                tempo_cpu = re.search(
                    r"Tempo de CPU:\s*(.*)",
                    bloco
                ).group(1).strip()

                uso_memoria = re.search(
                    r"Uso de Memória:\s*(.*)",
                    bloco
                ).group(1).strip()

                dados.append({
                    "Transformação": transformacao,
                    "Ferramenta": ferramenta,
                    "Dataset": dataset,
                    "Execução": execucao,
                    "Tempo de Resposta": tempo_resposta,
                    "Tempo de CPU": tempo_cpu,
                    "Uso de Memória": uso_memoria
                })

            except Exception as e:

                print(
                    f"Erro ao processar bloco "
                    f"do arquivo {arquivo}"
                )

                print(str(e))

    df = pd.DataFrame(dados)

    df.to_csv(
        ARQUIVO_SAIDA,
        index=False
    )

    print(
        f"CSV consolidado criado: "
        f"{ARQUIVO_SAIDA}"
    )