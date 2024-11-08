from .__loader__ import dataset
from logger import log
from sqlite3 import Connection
import datetime

def populate_artists(connection: Connection):
  log("Populating Artist table...")
  for index, row in dataset.iterrows():
    artists = row["artist(s)_name"].split(", ")
    for artist in artists:
      connection.execute("INSERT INTO Artist (name) VALUES (?)", (artist,))
  connection.commit()
  log("Populated Artist table")
  
def populate_vendors(connection: Connection):
  log("Populating Vendor table...")
  vendors = ['Spotify', 'Shazam', 'Apple', 'Deezer']
  for vendor in vendors:
    connection.execute("INSERT INTO Vendor (name) VALUES (?)", (vendor,))
  connection.commit()
  log("Populated Vendor table")
  
def populate_track(connection: Connection):
  log("Populating Track table...")
  for index, row in dataset.iterrows():
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
  connection.commit()
  log("Populated Track table")
  
def populate_stats(connection: Connection):
  log("Populating MusicalStats table...")
  for index, row in dataset.iterrows():
    connection.execute("""INSERT INTO MusicalStats (
      bpm,
      "key",
      "mode",
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
  connection.commit()
  log("Populated Track table")

def relate_track_to_artist(connection: Connection):
  for index, row in dataset.iterrows():
    artists = row["artist(s)_name"].split(", ")
    artists = [
      connection.execute("SELECT id FROM Artist WHERE name = (?)", (name,)).fetchall()[0][0]
      for name in artists
    ]
    
    for artist in artists:
      connection.execute("INSERT INTO Track_Artist (artist_id, track_id) VALUES (?, ?)", (artist, index,))
    connection.commit()
    
def relate_track_to_playlists(connection: Connection):
  vendors = ['Spotify', 'Apple', 'Deezer']
  for index, row in dataset.iterrows():
    for vendor in vendors:
      connection.execute("""INSERT INTO Track_Playlist (
        count,
        track_id,
        vendor_name
      ) VALUES (?, ?, ?)""", (
        row[f'in_{vendor.lower()}_playlists'],
        index,
        vendor
      ))
    connection.commit()
      
def relate_track_to_charts(connection: Connection):
  vendors = ['Spotify', 'Apple', 'Deezer', 'Shazam']
  for index, row in dataset.iterrows():
    for vendor in vendors:
      connection.execute("""INSERT INTO Track_Chart (
        count,
        track_id,
        vendor_name
      ) VALUES (?, ?, ?)""", (
        row[f'in_{vendor.lower()}_charts'],
        index,
        vendor
      ))
    connection.commit()
  