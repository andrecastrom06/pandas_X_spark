from pyspark.sql.functions import col
from pyspark.sql.types import DateType

# Conversão usando .cast()
df_ps = df_ps.withColumn('fecha_internacion', col('fecha_internacion').cast(DateType()))
