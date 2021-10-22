import config
import mysql.connector

def connection():
    connect = mysql.connector.connect(
            host = config.db_endpoint,
            user = config.db_username,
            password = config.db_password,
            database= config.db_name)
    cursor = connect.cursor()
    return cursor