-- Artist Collaborations --
-- Lists all artist collaborations and the number of tracks each collaboration appears on. --

SELECT GROUP_CONCAT(a.name, ', ') AS "collaboration", COUNT(t.id) AS track_count
FROM Track_Artist AS ta
JOIN Artist AS a ON ta.artist_id = a.id
JOIN Track AS t ON ta.track_id = t.id
GROUP BY t.id
HAVING COUNT(a.id) > 1
ORDER BY track_count DESC;
