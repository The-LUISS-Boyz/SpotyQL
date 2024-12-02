import pandas as pd
from utils import configuration

def clear_dataset(dataset: pd.DataFrame):
  """
  This function clears all NaN values from the dataset.
  We will use different approaches for different columns.
  """
  
  # for 'track_name', 'artist(s)_name' we will fill with empty strings
  dataset['track_name'] = dataset['track_name'].fillna('')
  dataset['artist(s)_name'] = dataset['artist(s)_name'].fillna('')
  
  # for 'streams' we will fill with 0
  dataset['streams'] = dataset['streams'].fillna(0)
  
  # for 'cover_url' we will fill with 'Not Found'
  dataset['cover_url'] = dataset['cover_url'].fillna('Not Found')
  
  # for 'released_year', 'released_month', 'released_day' we will simply drop the row
  dataset = dataset.dropna(subset=['released_year', 'released_month', 'released_day'])
  """
  Explanation:
    since 'released_year', 'released_month', 'released_day' form a date,
    filling them with 0s would produce incorrect results in some queries, where date related operations are required.
    Hence, we will simply drop the row.
  """
  
  # for vendors' information, we will fill with 0s
  dataset['in_spotify_playlists'] = dataset['in_spotify_playlists'].fillna(0)
  dataset['in_spotify_charts'] = dataset['in_spotify_charts'].fillna(0)
  dataset['in_apple_playlists'] = dataset['in_apple_playlists'].fillna(0)
  dataset['in_apple_charts'] = dataset['in_apple_charts'].fillna(0)
  dataset['in_deezer_playlists'] = dataset['in_deezer_playlists'].fillna(0)
  dataset['in_deezer_charts'] = dataset['in_deezer_charts'].fillna(0)
  dataset['in_shazam_charts'] = dataset['in_shazam_charts'].fillna(0)
  
  # finally, for music stats, we will fill with default values
  dataset['bpm'] = dataset['bpm'].fillna(0)
  dataset['key'] = dataset['key'].fillna('')
  dataset['mode'] = dataset['mode'].fillna('')
  dataset['danceability_%'] = dataset['danceability_%'].fillna(0)
  dataset['valence_%'] = dataset['valence_%'].fillna(0)
  dataset['energy_%'] = dataset['energy_%'].fillna(0)
  dataset['acousticness_%'] = dataset['acousticness_%'].fillna(0)
  dataset['speechiness_%'] = dataset['speechiness_%'].fillna(0)
  dataset['liveness_%'] = dataset['liveness_%'].fillna(0)
  dataset['instrumentalness_%'] = dataset['instrumentalness_%'].fillna(0)
  
  # drop song "Love Grows (Where My Rosemary Goes)"
  dataset = dataset[dataset['track_name'] != "Love Grows (Where My Rosemary Goes)"]
  """
  Explanation:
    This song has a broken attribute 'streams'.
    Since this is the only song with broken 'streams' attribute, we will simply drop it.
  Pros:
    This is a quick solution, and removes quite some code in the 'migration' process.
    Since we're doing this only once, it makes no sense to spend more time on this.
  Drawback:
    This is not a scalable solution, but since we're migrating the dataset, we can get away with this.
    In the instance of a real-time system, we would need to handle such cases.
  """
  
  return dataset

dataset = clear_dataset(pd.read_csv(configuration.dataset_path))