from . import Query
from .variables import *
import json
import os
from utils.Configuration import configuration

def load_queries():
  with open(SCHEMA_PATH, "r") as file:
    schema = json.load(file)
    
    for query in schema:
      if "file_path" in query:
        yield Query(
          name=query["name"],
          file_path=os.path.join(QUERIES_PATH, query["file_path"]),
          description=query["description"]
        )
      
      if configuration.database_type == "sqlite":
        if "file_path_sqlite" in query:
          yield Query(
            name=query["name"],
            file_path=os.path.join(QUERIES_PATH, query["file_path_sqlite"]),
            description=query["description"]
          )
      if configuration.database_type == "mysql":
        if "file_path_mysql" in query:
          yield Query(
            name=query["name"],
            file_path=os.path.join(QUERIES_PATH, query["file_path_mysql"]),
            description=query["description"]
          )
