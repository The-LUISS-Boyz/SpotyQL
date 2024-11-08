from .__loader__ import dataset
from utils import configuration
from .functions import *
from logger import log

def populate_database(connection):
  if configuration.done_population: return
  
  log("Populating database...")
  populate_artists(connection)
  populate_vendors(connection)
  populate_track(connection)
  populate_stats(connection)
  log("Populated database")
  
  log("Creating relations...")
  relate_track_to_artist(connection)
  relate_track_to_playlists(connection)
  relate_track_to_charts(connection)
  log("Created relations")
  
  configuration.done_population = True
  configuration.save()