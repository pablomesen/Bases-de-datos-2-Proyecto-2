# Utiliza la imagen base de Bitnami Spark
FROM bitnami/spark:3.5.3

# Cambia a usuario root para realizar la instalación de paquetes
USER root

# Instala 'curl' para descargar archivos
RUN install_packages curl

# Vuelve al usuario original de Spark
USER 1001

# Descargar el conector de Neo4j para Spark
RUN curl -L https://repo1.maven.org/maven2/org/neo4j/neo4j-connector-apache-spark_2.12/5.3.2_for_spark_3/neo4j-connector-apache-spark_2.12-5.3.2_for_spark_3.jar --output /opt/bitnami/spark/jars/neo4j-connector-apache-spark_2.12-5.3.2_for_spark_3.jar

