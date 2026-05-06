def exportar_metricas(nome_teste, ferramenta, metricas, arquivo_saida='metricas_resultados.txt'):
    """Salva os resultados em um arquivo TXT."""
    with open(arquivo_saida, 'a', encoding='utf-8') as f:
        f.write(f"--- Teste: {nome_teste} | Ferramenta: {ferramenta} ---\n")
        f.write(f"Tempo de Resposta: {metricas['tempo_resposta']} s\n")
        f.write(f"Tempo de CPU: {metricas['tempo_cpu']} s\n")
        f.write(f"Uso de Memória: {metricas['memoria_pico']} MB\n")
        f.write("-" * 50 + "\n\n")

# Exemplo de chamada:
# exportar_metricas("Leitura CSV", "Pandas", metricas)
