from .functions import get_info, on_load, get_context, execute_query, execute_query_str
from sql import get_connection

class Api:
  def __init__(self):
    pass
  
  def get_info(self):
    return get_info()
  
  def on_load(self):
    on_load(get_connection())
  
  def get_context(self):
    return get_context()

  def execute_query(self, index):
    return execute_query(get_connection(), index)

  def execute_query_str(self, text: str):
    return execute_query_str(get_connection(), text)