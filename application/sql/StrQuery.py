import sqlite3
from tabulate import tabulate
from utils.Configuration import configuration

if configuration.database_type == "sqlite":
  from sql.__sqlite__ import execute_and_fetch
else:
  from sql.__mysql__ import execute_and_fetch

class StrQuery:
  text: str
  
  def __init__(self, text: str):
    self.text = text

  @property
  def code(self):
    with open(self.file_path, "r") as file:
      return self.text
    
  def execute_statement(self, connection: sqlite3.Connection):
    cursor = connection.cursor()
    
    rows = execute_and_fetch(cursor, self.text)
    columns = [d[0] for d in cursor.description]
    
    return tabulate(rows, headers=columns, tablefmt="grid")