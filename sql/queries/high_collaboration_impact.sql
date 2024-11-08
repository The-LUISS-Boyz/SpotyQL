-- 8. Artists with High Collaboration Rates and Their Impact on Streams --
-- Query: Find artists with an average artist_count > 2 (count of distinct artists per track) and the average streams of their songs. --

SELECT a.name AS artist_name, 
       COUNT(DISTINCT ta.track_id) / COUNT(DISTINCT a.id) AS avg_collaborators, 
       AVG(t.streams) AS avg_streams
FROM Artist a
JOIN Track_Artist ta ON a.id = ta.artist_id
JOIN track t ON ta.track_id = t.name
GROUP BY a.name
HAVING avg_collaborators > 2
ORDER BY avg_streams DESC;
