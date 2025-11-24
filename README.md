# 🐼Pandas vs Spark⚡
[📄 Relatório Completo](https://docs.google.com/document/d/1gVG3Z7nUAXxYFjGq1yjq_GWUupYNv8vFHKQhjC8c6io/edit?usp=sharing)

Este projeto compara **Pandas** e **Apache Spark** usando dados do ENEM para medir desempenho em operações pesadas. As métricas analisadas foram: **tempo de CPU**, **tempo total**, **consumo de memória** e **latência**.

O objetivo é mostrar, de forma prática, **quando vale usar Pandas** e **quando Spark entrega um resultado melhor**.

---

## Quando usar Pandas?

Pandas funciona muito bem quando os dados **cabem na RAM** e o processamento é simples.

**Pontos fortes:**
- Rápido para datasets pequenos ou médios  
- Sintaxe simples  
- Integração total com Python  
- Sem necessidade de engine ou cluster  

**Limitações observadas nos testes:**
- Consumo acima de **2.6 GB de RAM**  
- Execuções ultrapassando **80 segundos** em algumas operações  
- Carrega o dataset inteiro em memória → não escala  

**Use Pandas quando:**
- O arquivo cabe tranquilamente na RAM  
- Você está fazendo análise exploratória ou prototipagem  
- As operações são diretas  

**Evite Pandas quando:**
- Os arquivos são grandes  
- O processamento é intenso  
- A aplicação precisa escalar  

---

## Quando usar Spark?

Spark foi projetado para grandes volumes de dados e desempenho distribuído, mesmo rodando localmente já mostra ganhos claros.

**Resultados dos testes:**
- CPU quase insignificante  
- Menos de **1 MB de RAM** utilizada  
- Execução consideravelmente mais rápida que Pandas  
- Latência muito menor em operações pesadas  

**Pontos fortes do Spark:**
- Processamento em partes (não carrega tudo na RAM)  
- Aproveita múltiplos núcleos  
- Excelente para filtros pesados e agregações  
- Escalável desde o ambiente local até clusters distribuídos  

**Desvantagem:**
- Overhead inicial ao iniciar a sessão  

**Use Spark quando:**
- Os dados são grandes  
- O processamento é complexo ou recorrente  
- Você precisa de velocidade em escala  

**Evite Spark quando:**
- O dataset é pequeno  
- O script é curto e simples  
- O overhead inicial não compensa  

---

## 📊 Comparativo dos Testes

### Média das notas de redação
| Métrica | Pandas | Spark |
|--------|--------|--------|
| Tempo de CPU | 55.1094s | 0.0312s |
| Tempo total | 66.5289s | 36.6717s |
| Memória | 2626.18 MB | 0.83 MB |
| Latência | 66.4123s | 25.4116s |

### Média da redação (quem tirou >900 em Matemática), agrupado por estado
| Métrica | Pandas | Spark |
|--------|--------|--------|
| Tempo de CPU | 70.8125s | 0.0625s |
| Tempo total | 81.6552s | 36.6837s |
| Memória | 2629.39 MB | 0.3 MB |
| Latência | 81.5080s | 22.3862s |

---

## Conclusão

- **Spark é melhor para bases grandes, operações intensas e cenários que exigem escalabilidade**, consumindo até **8.000x menos memória** e executando em **menos da metade do tempo**.  
- **Pandas é perfeito para bases pequenas e manipulação rápida**, mas perde desempenho rapidamente quando os arquivos passam de alguns GB.

---
