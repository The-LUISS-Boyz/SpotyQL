-- Tracks with Highest Playlist Count per Vendor --
-- Finds the track(s) with the highest playlist count for each vendor, showing the most featured tracks on each platform. --

SELECT vendor_name, t.name, MAX(count) AS playlists
FROM Track_Playlist AS tc
JOIN Track AS t ON tc.track_id = t.id
GROUP BY vendor_name
ORDER BY playlists DESC;
