# TCC — Benchmark Pandas vs PySpark

Comparativo de desempenho entre **Pandas** e **PySpark** em operações de manipulação de dados sobre datasets de casos de COVID-19 da Argentina, em diferentes volumetrias.

## Objetivo

Avaliar o comportamento de Pandas e PySpark em transformações equivalentes, registrando tempo de execução, consumo de CPU e uso de memória, para apoiar a análise de qual ferramenta se comporta melhor conforme o volume de dados e o tipo de operação.

## Estrutura do projeto

```
Parte Pratica/
├── code/                    # Scripts de benchmark
│   ├── code_import/
│   │   ├── executor.py      # Orquestração central dos testes
│   │   ├── metricas.py      # Coleta de tempo, CPU e memória
│   │   └── result.py        # Exportação dos resultados em .txt
│   ├── run.sh               # Executa todos os benchmarks em sequência
│   └── *.py                 # Um script por transformação
├── data/                    # Datasets CSV (não versionados)
├── result_local/            # Resultados do ambiente local
├── result_distribuidos/     # Resultados do ambiente distribuído
├── consolidado_result.py    # Consolida .txt em CSV
└── requirements.txt
```

## Datasets

Quatro arquivos CSV, executados nesta ordem:

| Arquivo | Descrição |
|---|---|
| `covid_2020_2021_200.csv` | Subconjunto (~200 MB) |
| `covid_2020_2021_600.csv` | Subconjunto (~600 MB) |
| `covid_2020_2021_1800.csv` | Subconjunto (~1,8 GB) |
| `Covid19Casos.csv` | Dataset completo (~6 GB) |

## Transformações avaliadas

Cada operação possui implementação equivalente em Pandas e Spark:

| Script | Transformação | Arquivo de saída |
|---|---|---|
| `ler.py` | Contagem de linhas | `count_rows.txt` |
| `select_columns.py` | Seleção de colunas | `select_columns.txt` |
| `rename_drop.py` | Renomear e eliminar colunas | `rename_drop.txt` |
| `cast.py` | Conversão de tipos | `cast.txt` |
| `filtrar.py` | Filtros condicionais | `filter.txt` |
| `order_by.py` | Ordenação | `orderby.txt` |
| `join.py` | Join entre colunas do mesmo dataset | `join.txt` |
| `agrupamento.py` | GroupBy com count, min, max e avg | `groupby.txt` |
| `criar_csv.py` | Criação e descarte de DataFrame | `create_drop.txt` |
| `escrever.py` | Inserção e remoção de linha | `insert_drop_row.txt` |

## Métricas coletadas

Cada execução registra, em arquivos `.txt` dentro de `result_local/` (ou `result_distribuidos/`):

| Métrica | Descrição |
|---|---|
| **Tempo de Leitura CSV** | Tempo para carregar o dataset (medido separadamente) |
| **Tempo de Inicialização Spark** | Tempo do `SparkSession.getOrCreate()` (apenas Spark, uma vez por script) |
| **Tempo de Resposta** | Tempo da transformação em si (métrica principal) |
| **Tempo Total** | Soma das fases aplicáveis (leitura + init Spark + transformação) |
| **Tempo de CPU** | Tempo de CPU consumido pelo processo Python no intervalo da transformação |
| **Uso de Memória** | RSS do processo Python no instante final da transformação (MB) |

### O que entra em cada tempo

- **Pandas — Tempo de Resposta:** apenas a função de transformação (`funcao_pandas`).
- **Pandas — Tempo Total:** leitura CSV + Tempo de Resposta.
- **Spark — Tempo de Resposta:** apenas a função de transformação (`funcao_spark`), sobre dados já em cache.
- **Spark — Tempo Total:** inicialização Spark + leitura CSV + Tempo de Resposta.

A leitura do CSV e a inicialização do Spark **não entram** no Tempo de Resposta; são medidas à parte e compõem o Tempo Total.

### Como CPU e memória são medidas

Implementado em `code_import/metricas.py` com `psutil`:

- **CPU:** diferença de `cpu_times().user + cpu_times().system` entre início e fim da transformação (segundos de CPU, não percentual).
- **Memória:** valor de `memory_info().rss` no instante final da transformação.

## Protocolo experimental

### Ordem de execução

Definida em `code/run.sh`:

1. agrupamento → cast → criar_csv → escrever → filtrar → join → ler → order_by → rename_drop → select_columns

Dentro de cada script:

1. Bloco **Pandas** — 4 datasets × `NUM_EXECUCOES` repetições
2. Bloco **Spark** — 4 datasets × `NUM_EXECUCOES` repetições

Não há execuções de aquecimento (warm-up): todas as repetições são contabilizadas.

O número de repetições é controlado pela constante `NUM_EXECUCOES` em `code/code_import/executor.py` (atualmente **5**).

### Trecho cronometrado

O Tempo de Resposta corresponde exclusivamente ao intervalo entre `capturar_metricas_inicio()` e `capturar_metricas_fim()`, envolvendo apenas a chamada da função de transformação.

### Comportamento específico do Spark

Antes de cada execução Spark:

1. Leitura do CSV (`read.csv` com `header=True`, `inferSchema=True`)
2. `cache()` + `count()` para materializar os dados (cronometrado como Tempo de Leitura CSV)
3. Execução da transformação sobre dados em cache
4. `unpersist()` ao final

Ações que materializam cada transformação Spark (dentro do Tempo de Resposta):

| Transformação | Materialização |
|---|---|
| count_rows | `count()` |
| select_columns | `count()` |
| rename_drop | `count()` |
| cast | `printSchema()` |
| filter | `count()` (dois filtros) |
| order_by | `count()` |
| join | `count()` |
| groupby | `collect()` |
| create_drop | `count()` |
| insert_drop_row | `count()` (após union e após filter) |

### Configuração do Spark

Definida em `code/code_import/executor.py`:

- **Modo:** `local[*]` (single-node, usa todos os núcleos lógicos da máquina)
- **Memória:** padrão do Spark (~1 GB), não configurada explicitamente
- **Partições:** padrão do Spark (200 em shuffles; leitura CSV proporcional ao tamanho do arquivo)

## Ambientes

Dois conjuntos de resultados, separados por pasta:

- `result_local/` — execução em máquina local
- `result_distribuidos/` — execução em ambiente distribuído

O mesmo código é utilizado em ambos; a diferença está no hardware onde os benchmarks foram rodados.

## Como executar

### Pré-requisitos

- Python 3.12+
- Java 17 (OpenJDK) — necessário para o PySpark
- Dependências: `pip install -r requirements.txt`

### Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

sudo apt install openjdk-17-jdk -y
java -version

cd code
bash run.sh
```

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Configurar Java (ajuste o caminho se necessário)
$env:JAVA_HOME = ".\.jdk\extracted\jdk-17.0.14+7"
$env:Path = "$env:JAVA_HOME\bin;" + $env:Path

cd code
@('agrupamento','cast','criar_csv','escrever','filtrar','join','ler','order_by','rename_drop','select_columns') | ForEach-Object { python "$_.py" }
```

### Consolidar resultados

Após os benchmarks, gera CSVs a partir dos `.txt`:

```bash
python consolidado_result.py
```

Saída: `result_local/benchmark_consolidado_local.csv` e `result_distribuidos/benchmark_consolidado_distribuidos.csv`.

## Limitações conhecidas

- Não há timeout programático por execução.
- Não há captura automática de falhas (OOM, exceções); execuções com erro interrompem o script sem registro estruturado.
- A métrica de memória reflete o RSS no instante final, não um pico amostrado durante toda a execução.
- A transformação `cast` no Spark usa `printSchema()`, que não materializa o dataset completo.
