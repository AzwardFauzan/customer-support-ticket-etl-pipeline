from pyspark.sql import SparkSession
from pymongo import MongoClient

spark = SparkSession.builder \
    .appName("Customer Support ETL") \
    .getOrCreate()


df = spark.read.parquet("/opt/airflow/data/transform")


client = MongoClient("mongodb+srv://mongodb:mongodb@azward-playground.daxgg8h.mongodb.net/")
db_client = client["milestone_3"]
collection = db_client["customer-support-ticket"]

document_list = [
    row.asDict()
    for row in df.collect()
]

collection.insert_many(document_list)
client.close()