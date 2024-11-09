import sqlite3
from tabulate import tabulate

class StrQuery:
  text: str
  
  def __init__(self, text: str):
    self.text = text

  @property
  def code(self):
    with open(self.file_path, "r") as file:
      return self.text
    
  def execute_statement(self, connection: sqlite3.Connection):
    cursor = connection.cursor().execute(self.text)
    
    rows = cursor.fetchall()
    columns = [d[0] for d in cursor.description]
    
    return tabulate(rows, headers=columns, tablefmt="grid")