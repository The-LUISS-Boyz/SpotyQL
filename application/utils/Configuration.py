from json import load, dump
import os
from .variables import APPLICATION_PATH, CONFIGURATION_PATH

class Configuration:
  def __init__(self, path: str):
    self.path = path
    self.data = load(open(path))
    
  # frontend
  @property
  def frontend_path(self):
    return os.path.join(
      APPLICATION_PATH,
      self.data["frontend"]["path"]
    )
  
  # database
  @property
  def database_type(self):
    return self.data["database"]["type"]
  
  @property
  def database_sqlite_path(self):
    return os.path.join(APPLICATION_PATH, self.data["database"]["sqlite.path"])
  
  @property
  def database_mysql_host(self):
    return self.data["database"]["mysql.host"]
  @property
  def database_mysql_user(self):
    return self.data["database"]["mysql.user"]
  @property
  def database_mysql_password(self):
    return self.data["database"]["mysql.password"]
  @property
  def database_mysql_database(self):
    return self.data["database"]["mysql.database"]
  
  @property
  def database_sql_path(self):
    return os.path.join(APPLICATION_PATH, self.data["database"]["sql.path"])

  # dataset
  @property
  def dataset_path(self):
    return os.path.join(APPLICATION_PATH, self.data["dataset"]["path"])
  
  # info
  def get_info(self):
    return self.data["info"]

  # window
  @property
  def window_width(self):
    return self.data["window"]["width"]
  @property
  def window_height(self):
    return self.data["window"]["height"]
  
  # flags
  @property
  def done_migrations(self):
    return self.data.get("done_migrations", False)
  @done_migrations.setter
  def done_migrations(self, value: bool):
    self.data["done_migrations"] = value
  
  @property
  def done_population(self):
    return self.data.get("done_population", False)
  @done_population.setter
  def done_population(self, value: bool):
    self.data["done_population"] = value
  
  def save(self):
    dump(
      self.data,
      open(self.path, "w"),
      indent=4,
    )

configuration = Configuration(CONFIGURATION_PATH)