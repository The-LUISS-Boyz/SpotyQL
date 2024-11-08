-- 10. Top 5 Tracks Based on Total Streams with Platform Metrics --
-- Query: Identify Top 5 most streamed songs and show how popular the track is across platforms --

SELECT 
    t.name AS track_name,
    t.streams AS total_streams,
    t.in_spotify_playlists,
    t.in_spotify_charts,
    t.in_apple_playlists,
    t.in_apple_charts,
    t.in_deezer_playlists,
    t.in_deezer_charts,
    t.in_shazam_charts
FROM track t
ORDER BY t.streams DESC
LIMIT 5;
