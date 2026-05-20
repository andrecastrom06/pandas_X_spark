import re
import os
import pandas as pd

PASTA_RESULTADOS = "./result"

ARQUIVO_SAIDA = (
    "./result/benchmark_consolidado.csv"
)

dados = []

# lista txt da pasta
arquivos_txt = [
    os.path.join(PASTA_RESULTADOS, arq)
    for arq in os.listdir(PASTA_RESULTADOS)
    if arq.endswith(".txt")
]

for arquivo in arquivos_txt:

    print(f"Lendo: {arquivo}")

    # lê txt
    with open(arquivo, "r", encoding="utf-8") as f:

        conteudo = f.read()

    # separa blocos
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

# cria dataframe
df = pd.DataFrame(dados)

# salva csv
df.to_csv(
    ARQUIVO_SAIDA,
    index=False
)

print("CSV consolidado criado com sucesso.")

print(df.head())