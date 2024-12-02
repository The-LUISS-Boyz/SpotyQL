-- Tracks' average rank across all vendors' charts --
-- List tracks and their average rank across all vendors' charts. --

SELECT t.name, MAX(t.streams) AS streams, AVG(tc.count) AS average_rank
FROM Track_Chart AS tc
JOIN Track AS t ON tc.track_id = t.id
GROUP BY t.name
ORDER BY average_rank ASC, streams DESC;
