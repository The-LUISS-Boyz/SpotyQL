-- 6. Top 5 Most-Streamed Artists by Platform --
-- Query: For each platform (vendor), find the top 5 most-streamed artists and their total streams. --

SELECT t.vendor_name AS platform, a.name AS artist_name, SUM(t.streams) AS total_streams
FROM track t
JOIN Track_Artist ta ON t.name = ta.track_id
JOIN Artist a ON ta.artist_id = a.id
GROUP BY t.vendor_name, a.name
ORDER BY t.vendor_name, total_streams DESC
LIMIT 5;
