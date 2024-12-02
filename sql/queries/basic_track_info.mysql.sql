-- Basic Track Information --
-- Fetches basic information about each track, including name, artist(s), and release date. --

SELECT t.name, GROUP_CONCAT(a.name SEPARATOR ', ') AS "artist(s)", t.release_date
FROM Track_Artist AS ta
JOIN Track AS t ON ta.track_id = t.id
JOIN Artist AS a ON ta.artist_id = a.id
GROUP BY t.name, t.release_date;
