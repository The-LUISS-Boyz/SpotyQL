import mysql.connector
import mysql.connector.cursor
from utils.Configuration import configuration
from logger import log

def get_connection():
  try: 
    log("Connecting to MySQL server")
    
    return mysql.connector.connect(
      host=configuration.database_mysql_host,
    user=configuration.database_mysql_user,
      password=configuration.database_mysql_password,
      database=configuration.database_mysql_database
    )
  except mysql.connector.Error as e:
    log(f"Error connecting to MySQL server: {e}")
    log("Connecting to MySQL server and creating database")
    # connect to mysql server and create database
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=configuration.database_mysql_host,
        user=configuration.database_mysql_user,
        password=configuration.database_mysql_password
    )
    
    cursor = connection.cursor()
    
    # Create database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {configuration.database_mysql_database}")
    
    # Close the initial connection
    cursor.close()
    connection.close()
    log("Database created")
    
    return get_connection()

def execute_and_fetch(cursor: mysql.connector.cursor.MySQLCursor, command: str, params: tuple = ()):
  cursor.execute(command, params)
  return cursor.fetchall()