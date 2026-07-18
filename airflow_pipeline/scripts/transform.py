from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, to_timestamp

spark = SparkSession.builder \
    .appName("Customer Support ETL") \
    .getOrCreate()

# Membaca hasil extract
df = spark.read.parquet("/opt/airflow/data/raw")

df = df.withColumn(
    "Date_of_Purchase",
    to_timestamp("Date_of_Purchase", "yyyy-MM-dd")
)

df = df.withColumn(
    "First_Response_Time",
    to_timestamp("First_Response_Time", "yyyy-MM-dd HH:mm:ss")
)

df = df.withColumn(
    "Time_to_Resolution",
    to_timestamp("Time_to_Resolution", "yyyy-MM-dd HH:mm:ss")
)

df.write \
    .mode("overwrite") \
    .parquet("/opt/airflow/data/transform")