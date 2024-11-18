from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Conexión a Spark desde PySpark") \
        .master("spark://localhost:7077") \
         .config("spark.some.config.option", "config-value") \
         .getOrCreate()

print(spark.version)

df = spark.range(100).toDF("number")
df.show()