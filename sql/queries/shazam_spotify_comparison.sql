-- 9. Songs with High Shazam Rankings and Their Spotify Streams --
-- Query: Identify songs in the top 10 Shazam charts and compare their Spotify streams. --

SELECT t.name AS track_name, v.name AS vendor_name, t.streams
FROM track t
JOIN Vendor v ON t.vendor_name = v.name
WHERE v.name = 'Shazam'
ORDER BY t.streams DESC
LIMIT 10;
