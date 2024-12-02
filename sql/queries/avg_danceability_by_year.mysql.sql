-- Average Danceability by Release Year --
-- Calculates the average danceability of tracks released each year, providing a year-over-year look at this characteristic. --

SELECT 
  YEAR(release_date) AS release_year,
  AVG(danceability) AS avg_danceability
FROM MusicalStats
INNER JOIN Track ON Track.id = MusicalStats.track_id
GROUP BY release_year;
