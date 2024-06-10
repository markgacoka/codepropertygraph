from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def get_neo4j_connection(uri, auth):
    try:
        driver = GraphDatabase.driver(uri, auth=auth)
        driver.verify_connectivity()
        return driver
    except ServiceUnavailable:
        return None
