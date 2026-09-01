import re
import os
import pandas as pd

pastas = ["local", "distribuidos"]


def extrair_campo(bloco, padrao):
    match = re.search(padrao, bloco)
    return match.group(1).strip() if match else None


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

            ferramenta = extrair_campo(
                bloco,
                r"Ferramenta:\s*(.*)"
            )

            if not ferramenta:
                continue

            try:

                dados.append({
                    "Transformação": transformacao,
                    "Ferramenta": ferramenta,
                    "Dataset": extrair_campo(
                        bloco,
                        r"Dataset:\s*(.*)"
                    ),
                    "Execução": extrair_campo(
                        bloco,
                        r"Execução:\s*(.*)"
                    ),
                    "Tempo de Leitura CSV": extrair_campo(
                        bloco,
                        r"Tempo de Leitura CSV:\s*(.*)"
                    ),
                    "Tempo de Inicialização Spark": extrair_campo(
                        bloco,
                        r"Tempo de Inicialização Spark:\s*(.*)"
                    ),
                    "Tempo de Resposta": extrair_campo(
                        bloco,
                        r"Tempo de Resposta:\s*(.*)"
                    ),
                    "Tempo Total": extrair_campo(
                        bloco,
                        r"Tempo Total:\s*(.*)"
                    ),
                    "Tempo de CPU": extrair_campo(
                        bloco,
                        r"Tempo de CPU:\s*(.*)"
                    ),
                    "Uso de Memória": extrair_campo(
                        bloco,
                        r"Uso de Memória:\s*(.*)"
                    ),
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
        f"{ARQUIVO_SAIDA} "
        f"({len(df)} registros)"
    )
