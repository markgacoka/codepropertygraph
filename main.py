import os
from dotenv import load_dotenv
from codepropertygraph import get_neo4j_connection

load_dotenv()
USERNAME = os.environ["NEO4J_USERNAME"]
PASSWORD = os.environ["NEO4J_PASSWORD"]
URI = "neo4j+s://cb8ae961.databases.neo4j.io"

# Attempt to get a connection
driver = get_neo4j_connection(URI, (USERNAME, PASSWORD))

# If the connection is successful, you can use the driver
if driver:
    with driver.session(database="neo4j") as session:
        result = session.run("MATCH (n) RETURN count(n) AS node_count")
        
        # Fetch the single result
        node_count = result.single()["node_count"]
        
        # Print the number of nodes
        print(f"Number of nodes in the database: {node_count}")
    
    driver.close()