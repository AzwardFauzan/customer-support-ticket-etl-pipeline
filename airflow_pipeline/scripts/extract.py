import kagglehub
import os
from pyspark.sql import SparkSession

DATASET_ROOT_DIR = "/opt/airflow/data/"

# Download dataset
path = kagglehub.dataset_download(
    "muqaddasejaz/customer-support-ticket-dataset"
)

print("Path to dataset files:", path)

# Membuat folder jika belum ada
if not os.path.exists(DATASET_ROOT_DIR):
    os.makedirs(DATASET_ROOT_DIR)

# Copy dataset ke folder Airflow
os.system("cp -r {}/* {}".format(path, DATASET_ROOT_DIR))

# Membuat Spark Session
spark = SparkSession.builder \
    .appName("Customer Support ETL") \
    .getOrCreate()

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("multiLine", "true") \
    .option("quote", '"') \
    .option("escape", '"') \
    .csv("/opt/airflow/data/customer_support_tickets.csv")

# Rename semua kolom yang mengandung spasi
df = df.toDF(*[
    col.replace(" ", "_")
    for col in df.columns
])

df.write \
    .mode("overwrite") \
    .parquet("/opt/airflow/data/raw")
print("Raw data berhasil disimpan")

print("Jumlah data:", df.count())