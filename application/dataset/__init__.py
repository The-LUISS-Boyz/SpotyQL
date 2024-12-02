from .__loader__ import dataset
from utils import configuration
from .functions import *
from logger import log
from sqlite3 import Connection
from mysql.connector import MySQLConnection
from typing import Union

def populate_database(connection: Union[Connection, MySQLConnection]):
  if configuration.done_population: return
  cursor = connection.cursor()
  
  log("Populating database...")
  populate_artists(cursor)
  connection.commit()
  
  populate_vendors(cursor)
  connection.commit()
  
  populate_track(cursor)
  connection.commit()
  
  populate_stats(cursor)
  connection.commit()
  
  log("Populated database")
  
  log("Creating relations...")
  relate_track_to_artist(cursor)
  connection.commit()
  
  relate_track_to_playlists(cursor)
  connection.commit()
  
  relate_track_to_charts(cursor)
  connection.commit()
  
  log("Created relations")
  
  configuration.done_population = True
  configuration.save()