-- 3. Cross-Platform Popularity and Musical Characteristics Analysis --
-- Query: For songs that appear in the top 50 on all platforms (stored in Vendor and Track relationships), display their musical attributes. --

SELECT t.name AS track_name, ms.bpm, ms.danceability, ms.energy, ms.valence, ms.acousticness, ms.instrumentalness
FROM track t
JOIN MusicalStats ms ON t.name = ms.track_name
WHERE t.vendor_name IN ('Spotify', 'Apple Music', 'Deezer', 'Shazam')
AND t.streams >= (SELECT streams FROM track WHERE vendor_name = t.vendor_name ORDER BY streams DESC LIMIT 50)
GROUP BY t.name
ORDER BY t.streams DESC;
