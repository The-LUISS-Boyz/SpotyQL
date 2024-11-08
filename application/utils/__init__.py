from .Configuration import configuration
from .variables import *

context = {
  "name": configuration.get_info()["name"],
  "version": configuration.get_info()["version"],
  "path": configuration.frontend_path,
  "authors": configuration.get_info()["authors"],
  "logs": []
}