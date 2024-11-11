-- Top 5 Artists by Total Playlist Features --
-- Identifies the top 5 artists by total playlist count across all vendors, highlighting the most consistently featured artists. --

SELECT 
  Artist.name,
  SUM(Track_Playlist.count) AS total_playlists
FROM Artist
INNER JOIN Track_Artist ON Artist.id = Track_Artist.artist_id
INNER JOIN Track_Playlist ON Track_Artist.track_id = Track_Playlist.track_id
GROUP BY Artist.name
ORDER BY total_playlists DESC LIMIT 5;
