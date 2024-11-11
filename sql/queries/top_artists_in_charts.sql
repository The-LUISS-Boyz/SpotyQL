-- Most Frequently Featured Artists in Top Chart Positions --
-- Lists artists with the highest number of tracks appearing in the top 10 chart positions across all vendors. --

SELECT
  Artist.name,
  COUNT(*) AS top_10_tracks
FROM Artist
INNER JOIN Track_Artist ON Artist.id = Track_Artist.artist_id
INNER JOIN Track_Chart ON Track_Artist.track_id = Track_Chart.track_id
WHERE Track_Chart.count <= 10
GROUP BY Artist.name
ORDER BY top_10_tracks DESC;
