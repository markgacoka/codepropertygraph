import os, sys
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from neo4j.exceptions import ServiceUnavailable

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from codepropertygraph.engine import get_neo4j_connection

# Load environment variables from .env file
load_dotenv()

@patch('neo4j.GraphDatabase.driver')
def test_get_neo4j_connection_success(mock_driver):
    # Setup the mock
    mock_driver_instance = MagicMock()
    mock_driver.return_value = mock_driver_instance

    uri = "neo4j+s://cb8ae961.databases.neo4j.io"
    auth = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    # Call the function
    driver = get_neo4j_connection(uri, auth)

    # Assertions
    mock_driver.assert_called_once_with(uri, auth=auth)
    mock_driver_instance.verify_connectivity.assert_called_once()
    assert driver == mock_driver_instance

@patch('neo4j.GraphDatabase.driver')
def test_get_neo4j_connection_failure(mock_driver):
    mock_driver.side_effect = ServiceUnavailable

    uri = "neo4j+s://cb8ae961.databases.neo4j.io"
    auth = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    # Call the function
    driver = get_neo4j_connection(uri, auth)

    # Assertions
    mock_driver.assert_called_once_with(uri, auth=auth)
    assert driver is None
