import sqlite3

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
    return connection.executescript(self.code).fetchall()
