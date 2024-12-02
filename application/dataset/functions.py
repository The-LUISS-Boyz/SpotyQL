from .__loader__ import dataset
from logger import log
from sqlite3 import Cursor
from mysql.connector import MySQLConnection
from sql import execute_and_fetch
from typing import Union
from utils.Configuration import configuration
import datetime

def populate_artists(connection: Union[Cursor, MySQLConnection]):
  log("Populating Artist table...")
  
  for index, row in dataset.iterrows():
    artists = row["artist(s)_name"].split(", ")
    for artist in artists:
      if configuration.database_type == "sqlite":
        connection.execute("INSERT INTO Artist (name) VALUES (?)", (artist,))
      else:
        connection.execute("INSERT INTO Artist (name) VALUES (%s)", (artist,))
  #connection.commit()
  log("Populated Artist table")
  
def populate_vendors(connection: Union[Cursor, MySQLConnection]):
  log("Populating Vendor table...")
  vendors = ['Spotify', 'Shazam', 'Apple', 'Deezer']
  for vendor in vendors:
    if configuration.database_type == "sqlite":
      connection.execute("INSERT INTO Vendor (name) VALUES (?)", (vendor,))
    else:
      connection.execute("INSERT INTO Vendor (name) VALUES (%s)", (vendor,))
  #connection.commit()
  log("Populated Vendor table")
  
def populate_track(connection: Union[Cursor, MySQLConnection]):
  log("Populating Track table...")
  for index, row in dataset.iterrows():
    # for sqlite implementation
    if configuration.database_type == "sqlite":
      connection.execute("""INSERT INTO Track (
        id,
        name,
        streams,
        release_date,
        cover_url
      ) VALUES (?, ?, ?, ?, ?)""", (
        index,
        row['track_name'],
        row["streams"],
        datetime.datetime(
          row["released_year"],
          row["released_month"],
          row["released_day"]
        ),
        row["cover_url"],
      ))
    # for mysql implementation
    else:
      connection.execute("""INSERT INTO Track (
        id,
        name,
        streams,
        release_date,
        cover_url
      ) VALUES (%s, %s, %s, %s, %s)""", (
        index,
        row['track_name'],
        row["streams"],
        datetime.datetime(
          row["released_year"],
          row["released_month"],
          row["released_day"]
        ),
        row["cover_url"],
      ))
  #connection.commit()
  log("Populated Track table")
  
def populate_stats(connection: Union[Cursor, MySQLConnection]):
  log("Populating MusicalStats table...")
  for index, row in dataset.iterrows():
    if configuration.database_type == "sqlite":
      connection.execute("""INSERT INTO MusicalStats (
        bpm,
        `key`,
        `mode`,
        valence,
        danceability,
        energy,
        acousticness,
        instrumentalness,
        liveness,
        speechiness,
        track_id
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
        row["bpm"],
        row["key"],
        row["mode"],
        row["valence_%"],
        row["danceability_%"],
        row["energy_%"],
        row["acousticness_%"],
        row["instrumentalness_%"],
        row["liveness_%"],
        row["speechiness_%"],
        index,
      ))
    else:
      connection.execute("""INSERT INTO MusicalStats (
        bpm,
        `key`,
        `mode`,
        valence,
        danceability,
        energy,
        acousticness,
        instrumentalness,
        liveness,
        speechiness,
        track_id
      ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
        row["bpm"],
        row["key"],
        row["mode"],
        row["valence_%"],
        row["danceability_%"],
        row["energy_%"],
        row["acousticness_%"],
        row["instrumentalness_%"],
        row["liveness_%"],
        row["speechiness_%"],
        index,
      ))
  #connection.commit()
  log("Populated Track table")

def relate_track_to_artist(connection: Union[Cursor, MySQLConnection]):
  artist_command = "SELECT id FROM Artist WHERE name = (?)" if configuration.database_type == "sqlite" else \
                   "SELECT id FROM Artist WHERE name = (%s)"
  insert_command = "INSERT INTO Track_Artist (artist_id, track_id) VALUES (?, ?)" if configuration.database_type == "sqlite" else \
                   "INSERT INTO Track_Artist (artist_id, track_id) VALUES (%s, %s)"
  
  for index, row in dataset.iterrows():
    artists = row["artist(s)_name"].split(", ")
    artists = [
      execute_and_fetch(connection, artist_command, (name,))[0][0]
      for name in artists
    ]
    
    for artist in artists:
      connection.execute(insert_command, (artist, index))
  #connection.commit()
    
def relate_track_to_playlists(connection: Union[Cursor, MySQLConnection]):
  vendors = ['Spotify', 'Apple', 'Deezer']
  insert_command = "INSERT INTO Track_Playlist (count, track_id, vendor_name) VALUES (?, ?, ?)" if configuration.database_type == "sqlite" else \
                   "INSERT INTO Track_Playlist (count, track_id, vendor_name) VALUES (%s, %s, %s)"
  for index, row in dataset.iterrows():
    for vendor in vendors:
      connection.execute(insert_command, (
        int(str(row[f'in_{vendor.lower()}_playlists']).replace(',', '')),
        index,
        vendor
      ))
  #connection.commit()
      
def relate_track_to_charts(connection: Union[Cursor, MySQLConnection]):
  vendors = ['Spotify', 'Apple', 'Deezer', 'Shazam']
  insert_command = "INSERT INTO Track_Chart (count, track_id, vendor_name) VALUES (?, ?, ?)" if configuration.database_type == "sqlite" else \
                   "INSERT INTO Track_Chart (count, track_id, vendor_name) VALUES (%s, %s, %s)"
  for index, row in dataset.iterrows():
    for vendor in vendors:
      if isinstance(row[f'in_{vendor.lower()}_charts'], str):
        charts_info = row[f'in_{vendor.lower()}_charts'].replace(',', '')
      else:
        charts_info = row[f'in_{vendor.lower()}_charts']
        
      connection.execute(insert_command, (
        charts_info,
        index,
        vendor
      ))
  #connection.commit()