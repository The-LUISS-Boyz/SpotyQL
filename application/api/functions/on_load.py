from utils import configuration
from sql import migrations_query
import sqlite3
from logger import log

def on_load(connection: sqlite3.Connection):
  if not configuration.done_migrations:
    log("Executing migrations")
    migrations_query.execute(connection)
    configuration.done_migrations = True
    configuration.save()
    log("Migrations executed")
  else:
    log("Migrations already executed")
