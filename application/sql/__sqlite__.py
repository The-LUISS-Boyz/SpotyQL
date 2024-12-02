import sqlite3
from utils import configuration
import os
from logger import log

def get_connection():
  if not os.path.exists(configuration.database_sqlite_path):
    configuration.done_migrations = False
    configuration.done_population = False
    configuration.save()

  connection = sqlite3.connect(configuration.database_sqlite_path)
  log("Initialized database connection")
  return connection

def execute_and_fetch(cursor: sqlite3.Cursor, command: str, params: tuple = ()):
  cursor = cursor.execute(command, params)
  return cursor.fetchall()