from neo4j import GraphDatabase

# Connection to Neo4J Database
uri = "bolt://localhost:7687"

def check_connection():
    driver = GraphDatabase.driver(uri, auth=("neo4j", "badpassword"))    
    try:
        with driver.session() as session:
            result = session.run("RETURN 1")
            if result.single()[0] == 1:
                print("Conexión exitosa a la base de datos.")
                return driver
            else:
                print("Conexión fallida.")
                return None
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        driver.close()