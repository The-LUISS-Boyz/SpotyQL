from utils import configuration

def get_info():
  return [v for v in configuration.get_info().values()]
