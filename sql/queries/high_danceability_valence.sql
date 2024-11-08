-- 2. Songs with High Danceability and Valence that Are Also Chart-Toppers --
-- Query: Identify songs with danceability and valence above 70 and ranked within the top 20 on Spotify (assumed by highest streams). --

SELECT t.name AS track_name, t.streams, ms.danceability, ms.valence
FROM track t
JOIN MusicalStats ms ON t.name = ms.track_name
WHERE ms.danceability > 70 AND ms.valence > 70
ORDER BY t.streams DESC
LIMIT 20;
