import time
import psutil
import os


def medir_tempo():
    inicio = time.time()

    def fim():
        return round(time.time() - inicio, 4)

    return fim


def capturar_metricas_inicio():
    processo = psutil.Process(os.getpid())

    return {
        'tempo_inicio': time.time(),
        'cpu_inicio': (
            processo.cpu_times().user +
            processo.cpu_times().system
        ),
        'memoria_inicio': (
            processo.memory_info().rss / (1024 * 1024)
        )
    }


def capturar_metricas_fim(dados_inicio):
    processo = psutil.Process(os.getpid())

    tempo_fim = time.time()

    cpu_fim = (
        processo.cpu_times().user +
        processo.cpu_times().system
    )

    memoria_fim = (
        processo.memory_info().rss / (1024 * 1024)
    )

    return {
        'tempo_resposta': round(
            tempo_fim - dados_inicio['tempo_inicio'],
            4
        ),

        'tempo_cpu': round(
            cpu_fim - dados_inicio['cpu_inicio'],
            4
        ),

        'memoria_pico': round(memoria_fim, 2)
    }