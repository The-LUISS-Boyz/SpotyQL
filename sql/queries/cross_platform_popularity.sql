-- 3. Cross-Platform Popularity and Musical Characteristics Analysis --
-- Query: For songs that appear in the top 50 on all platforms (stored in Vendor and Track relationships), display their musical attributes. --

SELECT t.name AS track_name, streams, ms.bpm, ms.danceability, ms.energy, ms.valence, ms.acousticness, ms.instrumentalness
FROM track t
JOIN MusicalStats ms ON t.id = ms.track_id
WHERE t.id IN (
  SELECT tp.track_id
  FROM Track_Playlist AS tp
  JOIN Track_Chart AS tc ON tp.track_id = tc.track_id
  ORDER BY tp.count, tc.count DESC
  LIMIT 50
)
GROUP BY t.name
ORDER BY t.streams DESC;
