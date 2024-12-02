from .Query import Query
from .StrQuery import StrQuery
from .__loader__ import load_queries
from utils import configuration
from .variables import *

if configuration.database_type == "sqlite":
  from .__sqlite__ import get_connection, execute_and_fetch
elif configuration.database_type == "mysql":
  from .__mysql__ import get_connection, execute_and_fetch
else:
  raise NotImplementedError(f"Database type {configuration.database_type} not implemented")

migrations_query = Query("Migrations", "Migrations", MIGRATIONS_PATH)
queries = list(load_queries())