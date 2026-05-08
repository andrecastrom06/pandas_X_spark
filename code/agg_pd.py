import pandas as pd

from pandas_X_spark.code.metricas import (
    capturar_metricas_inicio,
    capturar_metricas_fim
)

from pandas_X_spark.code.result import exportar_metricas


# Executa 3 vezes
for i in range(1, 4):

    print(f"\nExecutando teste {i}...")

    # Captura início
    inicio = capturar_metricas_inicio()

    resumo_pd = df_casos.groupby(
        'residencia_provincia_nombre'
    ).agg({
        'id_evento_caso': 'count',
        'edad': ['min', 'max', 'mean']
    })

    # Renomeando colunas
    resumo_pd.columns = [
        'contagem',
        'idade_min',
        'idade_max',
        'idade_avg'
    ]

    # Captura métricas finais
    metricas = capturar_metricas_fim(inicio)

    # Exporta resultados
    exportar_metricas(
        nome_teste=f"Agregacao Pandas Execucao {i}",
        ferramenta="Pandas",
        metricas=metricas
    )

    print(metricas)