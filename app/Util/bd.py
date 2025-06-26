import psycopg2
from psycopg2 import OperationalError
import yaml
import os

# Obter o caminho absoluto usando o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'paramsBD.yml')

with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

def create_connection():
    """
    Create a connection to the PostgreSQL database.
    :return: Connection object or raises an exception
    """
    try:
        print(f"Attempting to connect to database: {config['db_name']} at {config['db_host']}:{config['db_port']}")
        connection = psycopg2.connect(
            database=config['db_name'],
            user=config['db_user'],
            password=config['db_password'],
            host=config['db_host'],
            port=config['db_port'],
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        print(f"Connection details: host={config['db_host']}, port={config['db_port']}, database={config['db_name']}, user={config['db_user']}")
        raise e

# Example usage:
# connection = create_connection("your_db_name", "your_db_user", "your_db_password", "your_db_host", "your_db_port")