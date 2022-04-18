# load in values from the .env file
import os
from dotenv import load_dotenv

# import Neo4J dependencies
from py2neo import Graph
from py2neo.ogm import GraphObject, Property, RelatedTo

# Set PATH for .env variable
PATH = os.getcwd()
load_dotenv(PATH + '\.env')

class Person(GraphObject):
    name=Property()
    age=Property()
    knows=RelatedTo('Person','KNOWS')

class CPGEngine:
    """
    An engine that creates nodes and relationships from input given.
    
    Input:
        __uri (str): The hostname to authenticate to the database.
        __user (str): The username used when authenticating into the database.
        __password (str): The database password.
        graph (obj): A graph object G(V, E) with node and edge information. 
    
    Returns:
        str: The name that identifies the graph.
    """
    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.graph = None
        
        try:
            # Ended up using a Graph than a driver to avoid errors if the driver closes wrongly.
            self.graph = Graph(self.__uri, auth=(self.__user, self.__password), name='neo4j')
        except Exception as e:
            print("Failed to locate the graph database:", e)
            
    def __str__(self):
        return self.graph.name
            
    def graph(self):
        # Return the graph object
        return self.graph
            
    def create_node(self, node):
        # Create a node given node information. Start a transaction and commit the changes.
        transaction = self.graph.begin()
        self.graph.create(node)
        self.graph.commit(transaction)
                    
    def create_relationship(self, rel):
        # Create a relationship between two nodes. Start a transaction and commit the changes.
        transaction = self.graph.begin()
        self.graph.create(rel)
        self.graph.commit(transaction)
    
    def get_all_nodes(self):
        # Return all nodes in the database
        return self.graph.nodes.match().all()
            
    def delete_all(self):
        # Delete all nodes and relationships from the database
        self.graph.delete_all()
            
            
if __name__ == '__main__':
    # Load the database credentials
    uri = os.getenv('NEO4JURI')
    user = os.getenv('NEO4JUSER')
    password = os.getenv('NEO4JPASS')
    
    # Initialize the engine
    engine = CPGEngine(uri, user, password)
    
    # Create a node and print all nodes as a result.
    engine.delete_all()
    
    alice = Person(name = 'Alice')
    keanu = Person(name = 'Keanu Reeves')  
    alice.knows.add(keanu)
    engine.graph.push(alice)
    engine.graph.push(keanu)
    
    # Display all nodes and query a Person object called Keanu Reeves
    all_nodes = engine.get_all_nodes()
    print("All nodes: ", all_nodes)
    print("Relationship types: ", list(engine.graph.schema.relationship_types))
    relationship = list(engine.graph.match(r_type='KNOWS'))
    print("All relationships: ", relationship)
    print("First Keanu: ", engine.graph.nodes.match("Person", name="Keanu Reeves").first())
