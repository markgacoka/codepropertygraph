import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

PATH = os.getcwd()
load_dotenv(PATH + '\.env')

class App:
    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        session = None
        response = None
        assert self.__driver is not None, "Driver not initialized!"
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

if __name__ == "__main__":
    uri = os.getenv('NEO4JURI')
    user = os.getenv('NEO4JUSER')
    password = os.getenv('NEO4JPASS')
    conn = App(uri=uri, user=user, password=password)
    conn.query("CREATE OR REPLACE DATABASE coradb")
    conn.close()