-- 1. Identify Artists with Consistently Popular Songs Across Multiple Years:
-- Query: Retrieve artists who have had songs in the top 50 charts for at least three different years, along with the number of years they’ve charted. --

SELECT a.name AS artist_name, COUNT(DISTINCT strftime('%Y', t.release_date)) AS years_in_top_50
FROM Artist a
JOIN Track_Artist ta ON a.id = ta.artist_id
JOIN Track t ON ta.track_id = t.id
JOIN Track_Chart tc ON t.id = tc.track_id
WHERE tc.count <= 50
GROUP BY a.name
HAVING years_in_top_50 >= 3
ORDER BY years_in_top_50 DESC;
