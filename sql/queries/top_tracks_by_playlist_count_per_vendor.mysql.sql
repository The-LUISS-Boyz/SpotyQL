-- Tracks with Highest Playlist Count per Vendor --
-- Finds the track(s) with the highest playlist count for each vendor, showing the most featured tracks on each platform. --

SELECT vendor_name, t.name, tc.playlists
FROM (
    SELECT vendor_name, track_id, MAX(count) AS playlists
    FROM Track_Playlist
    GROUP BY vendor_name, track_id
) AS tc
JOIN Track AS t ON tc.track_id = t.id
ORDER BY tc.playlists DESC;
