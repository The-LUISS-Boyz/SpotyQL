from . import Query
from .variables import *
import json
import os

def load_queries():
  with open(SCHEMA_PATH, "r") as file:
    schema = json.load(file)
    
    for query in schema:
      yield Query(
        query["name"],
        query["description"],
        os.path.join(QUERIES_PATH, query["file_path"])
      )
