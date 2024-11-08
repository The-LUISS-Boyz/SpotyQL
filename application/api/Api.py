from .functions import get_info, on_load, get_context
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
