# Renomear
df_ps = df_ps.withColumnRenamed('sexo', 'genero')

# Agregar (Nova coluna com valor constante)
from pyspark.sql.functions import lit
df_ps = df_ps.withColumn('nova_coluna', lit(0))

# Eliminar
df_ps = df_ps.drop('col1')
