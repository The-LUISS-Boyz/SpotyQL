import sqlite3
from tabulate import tabulate

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
    
  def execute(self, connection: sqlite3.Connection):
    cursor = connection.cursor().executescript(self.code)
    return cursor.fetchall()
  
  def execute_statement(self, connection: sqlite3.Connection):
    cursor = connection.cursor().execute(self.code)
    
    rows = cursor.fetchall()
    columns = [d[0] for d in cursor.description]
    
    return tabulate(rows, headers=columns, tablefmt="grid")
    
  
    
    
