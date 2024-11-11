-- Year with Highest Average Chart Ranking --
-- Computes the average count value in Track_Chart for each release year and returns the year with the highest average ranking, indicating the year with the highest-performing tracks. --

SELECT 
  strftime('%Y', release_date) AS release_year, 
  AVG(count) AS avg_ranking 
FROM Track_Chart
INNER JOIN Track ON Track.id = Track_Chart.track_id
GROUP BY release_year
ORDER BY avg_ranking DESC LIMIT 1;
