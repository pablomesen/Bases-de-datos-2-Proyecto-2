from .neo4j_conn import check_connection
import pandas as pd

# Connection to Neo4J Database
driver = check_connection()

# Read CSV file and select needed columns
csv_file = "./datasets/04_Transactions.csv"
data = pd.read_csv(csv_file, usecols=["transaction_id", "product_id", "customer_id", "transaction_date", "standard_cost"])

# Clean data: remove rows with NaN in needed columns
data_subset = data.dropna(subset=["transaction_id", "product_id", "customer_id", "transaction_date", "standard_cost"])

# Remove "$" and convert 'standard_cost' to float
data_subset.loc[:, 'standard_cost'] = data_subset['standard_cost'].replace('[$.]', '', regex=True).replace('[,]', '.', regex=True).astype(float)

# Transform data to Neo4J nodes and relationships
def create_transaction_relationships(tx, customer_id, product_id, transaction_id, transaction_date, standard_cost):
    tx.run(
        """
        MERGE (c:Customer {customer_id: $customer_id})
        MERGE (p:Product {product_id: $product_id})
        MERGE (c)-[:TRANSACTION {transaction_id: $transaction_id, transaction_date: $transaction_date, standard_cost: $standard_cost}]->(p)
        """ ,
        customer_id=customer_id, product_id=product_id, transaction_id=transaction_id, transaction_date=transaction_date, standard_cost=standard_cost
    )

# Create nodes and relationships
# driver.session() is deprecated, not sure how manage it properly
with driver.session() as session:
    for index, row in data_subset.iterrows():
        session.execute_write(create_transaction_relationships, row["customer_id"], row["product_id"], row["transaction_id"], row["transaction_date"], row["standard_cost"])

driver.close()