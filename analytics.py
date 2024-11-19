from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Conexión a Spark desde PySpark") \
    .master("spark://localhost:7077") \
    .config("spark.executor.memory", "512m") \
    .config("spark.executor.cores", "1") \
    .config("spark.driver.memory", "512m") \
    .config("spark.jars", "neo4j-connector-apache-spark.jar") \
    .getOrCreate()

print(f"Versión de Spark: {spark.version}")

# Probar operación básica
df = spark.range(100).toDF("number")
df.show()