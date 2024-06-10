from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def get_neo4j_connection(uri, auth):
    try:
        driver = GraphDatabase.driver(uri, auth=auth)
        driver.verify_connectivity()
        print("Connection successful")
        return driver
    except ServiceUnavailable as e:
        print("Failed to connect to Neo4j:", e)
        return None
