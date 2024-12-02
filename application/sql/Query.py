import sqlite3
from mysql.connector import MySQLConnection
from tabulate import tabulate
from utils.Configuration import configuration
from typing import Union

if configuration.database_type == "sqlite":
  from sql.__sqlite__ import execute_and_fetch
elif configuration.database_type == "mysql":
  from sql.__mysql__ import execute_and_fetch

class Query:
  name: str
  description: str
  file_path: str
  
  def __init__(self, name: str, description: str, file_path: str):
    self.name = name
    self.description = description
    self.file_path = file_path

  @property
  def code(self):
    with open(self.file_path, "r") as file:
      return file.read()
    
  def execute(self, connection: Union[sqlite3.Connection, MySQLConnection]):
    if configuration.database_type == "sqlite":
      cursor: sqlite3.Cursor = connection.cursor().executescript(self.code)
      result = cursor.fetchall()
    elif configuration.database_type == "mysql":
      cursor = connection.cursor()
      result = []
      for r in cursor.execute(self.code, multi=True):
        result.append(r.fetchall())
    else:
      raise ValueError(f"Invalid database type: {configuration.database_type}")
    
    connection.commit()
    cursor.close()
    return result
  
  def execute_statement(self, connection: Union[sqlite3.Connection, MySQLConnection]):
    cursor = connection.cursor()
    
    rows = execute_and_fetch(cursor, self.code)
    columns = [d[0] for d in cursor.description]
    
    return tabulate(rows, headers=columns, tablefmt="grid")
    
  
    
    
