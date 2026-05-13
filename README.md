# TCC

## Metricas

- Tempo de Resposta (ou de Execução): Medido em segundos, é a principal métrica para avaliar a eficiência de cada funcionalidade. São tomadas três amostras de tempo para cada função e calculada a média.
- Uso de Memória: Medido em GB, avaliado especificamente no "processo integrador" para observar o consumo de recursos.
- Uso de CPU: Medido em porcentagem (%), também analisado no cenário integrador para comparar a carga de processamento.

## Cenários
1. Manipulação de CSV:
  - Leitura de arquivos.
  - Escrita de arquivos.

2. Manipulação de DataFrames (Operações Básicas):
  - Criação de DataFrames.
  - Select: Seleção de colunas específicas.
  - Agregar/Renomear/Eliminar colunas: Modificações na estrutura da tabela.
  - Cambio de tipo de colunas: Conversão de tipos de dados (ex: string para data).
  - Filtros: Filtro de filas e filtro de filas únicas (distinct).
  - Ordenação: Ordenação de filas.

3. Transformações e Agregações:
  - Joins: União de diferentes conjuntos de dados.
  - GroupBy: Agrupamento de dados.
  - Funções de Agregação: Count (contagem), Min (mínimo), Max (máximo) e AVG (média).

4. Processo Integrador (Caso de Uso Real):
- Um cenário que simula um fluxo de trabalho completo (ETL), unindo os dados de casos de COVID-19 da Argentina com dados geográficos de províncias para gerar um relatório final.

## Como Executar:
Configure um ambiente Linux, após isso crie uma venv com:
* python -m venv venv

Ative a venv com:
* source venv/bin/activate

Baixe as bibliotecas utilizadas no projeto:
* pip install -r requirements.txt

Baixe o Java para o Apache Spark
* sudo apt install openjdk-17-jdk -y

Confirme se baixou a versão 17:
* java -version

Rode o comando:
* bash ./run.sh