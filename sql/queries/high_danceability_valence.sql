-- 2. Songs with High Danceability and Valence that Are Also Chart-Toppers --
-- Query: Identify songs with danceability and valence above 70 and ranked within the top 20 on Spotify chart. --

SELECT t.name AS track_name, tc.count AS spotify_rank, t.streams, ms.danceability, ms.valence
FROM track t
JOIN MusicalStats ms ON t.id = ms.track_id
JOIN Track_Chart tc ON t.id = tc.track_id
WHERE ms.danceability > 70 
  AND ms.valence > 70 
  AND tc.vendor_name = 'Spotify' 
  AND tc.count <= 20
  AND tc.count > 0
ORDER BY tc.count ASC;
