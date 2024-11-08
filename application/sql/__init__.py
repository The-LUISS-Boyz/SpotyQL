from .Query import Query
from .__loader__ import load_queries
from utils import configuration
from .variables import *

if configuration.database_type == "sqlite":
  from .__sqlite__ import get_connection
else:
  from .__mysql__ import get_connection

migrations_query = Query("Migrations", "Migrations", MIGRATIONS_PATH)
queries = list(load_queries())