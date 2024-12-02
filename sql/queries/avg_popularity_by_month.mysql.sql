-- Average Popularity (Track Count) by Release Month --
-- Calculates the average number of playlist features for tracks released in each month, indicating seasonal popularity trends. --

SELECT 
  CASE MONTH(release_date)
    WHEN 1 THEN 'January'
    WHEN 2 THEN 'February'
    WHEN 3 THEN 'March'
    WHEN 4 THEN 'April'
    WHEN 5 THEN 'May'
    WHEN 6 THEN 'June'
    WHEN 7 THEN 'July'
    WHEN 8 THEN 'August'
    WHEN 9 THEN 'September'
    WHEN 10 THEN 'October'
    WHEN 11 THEN 'November'
    WHEN 12 THEN 'December'
  END AS release_month,
  AVG(count) AS avg_playlist_count
FROM Track_Playlist
INNER JOIN Track ON Track.id = Track_Playlist.track_id
GROUP BY release_month
ORDER BY FIELD(release_month, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');
