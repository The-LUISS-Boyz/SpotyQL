-- 1. Identify Artists with Consistently Popular Songs Across Multiple Years:
-- Query: Retrieve artists who have had songs in the top 50 Spotify charts (assumed based on streams) for at least three different years, along with the number of years they’ve charted. --

SELECT a.name AS artist_name, COUNT(DISTINCT EXTRACT(YEAR FROM t.release_date)) AS years_in_top_50
FROM Artist a
JOIN Track_Artist ta ON a.id = ta.artist_id
JOIN Track t ON ta.track_id = t.id  
WHERE t.streams >= (SELECT streams FROM Track ORDER BY streams DESC LIMIT 50)
GROUP BY a.name
HAVING years_in_top_50 >= 3
ORDER BY years_in_top_50 DESC;
