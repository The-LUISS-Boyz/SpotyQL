-- Correlation Analysis Between Playlist Count and Chart Ranking --
-- Analyzes the correlation between playlist count and chart ranking for each track, identifying potential patterns in playlist popularity and chart success. --

-- For simplicity, we consider only the Spotify chart --
SELECT
  Track.name AS track_name,
  SUM(Track_Playlist.count) AS playlist_count,
  MAX(Track_Chart.count) AS chart_ranking
FROM Track_Playlist
INNER JOIN Track_Chart ON Track_Playlist.track_id = Track_Chart.track_id
JOIN Track ON Track.id = Track_Playlist.track_id
WHERE Track_Chart.vendor_name = 'Spotify'
AND   Track_Chart.count >= 1
GROUP BY Track_Playlist.track_id, Track.name
ORDER BY chart_ranking;
