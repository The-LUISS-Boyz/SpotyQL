from utils import configuration
import os

SQL_PATH = configuration.database_sql_path
QUERIES_PATH = os.path.join(SQL_PATH, "queries")
SCHEMA_PATH = os.path.join(QUERIES_PATH, "$schema.json")
MIGRATIONS_PATH = os.path.join(SQL_PATH, "migrations.sql")
