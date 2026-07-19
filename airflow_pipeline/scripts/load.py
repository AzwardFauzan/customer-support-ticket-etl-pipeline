from pyspark.sql import SparkSession
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() #load environment variables from .env file

spark = SparkSession.builder \
    .appName("Customer Support ETL") \
    .getOrCreate()


df = spark.read.parquet("/opt/airflow/data/transform")


client = MongoClient(os.getenv("MONGODB_URI"))
db_client = client["milestone_3"]
collection = db_client["customer-support-ticket"]

document_list = [
    row.asDict()
    for row in df.collect()
]

collection.insert_many(document_list)
client.close()
