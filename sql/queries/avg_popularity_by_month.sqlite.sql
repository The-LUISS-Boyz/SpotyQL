-- Average Popularity (Track Count) by Release Month --
-- Calculates the average number of playlist features for tracks released in each month, indicating seasonal popularity trends. --

SELECT 
  CASE strftime('%m', release_date)
    WHEN '01' THEN 'January'
    WHEN '02' THEN 'February'
    WHEN '03' THEN 'March'
    WHEN '04' THEN 'April'
    WHEN '05' THEN 'May'
    WHEN '06' THEN 'June'
    WHEN '07' THEN 'July'
    WHEN '08' THEN 'August'
    WHEN '09' THEN 'September'
    WHEN '10' THEN 'October'
    WHEN '11' THEN 'November'
    WHEN '12' THEN 'December'
  END AS release_month,
  AVG(count) AS avg_playlist_count
FROM Track_Playlist
INNER JOIN Track ON Track.id = Track_Playlist.track_id
GROUP BY release_month
ORDER BY strftime('%m', release_date);
