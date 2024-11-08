-- 7. Comparing Energy and Acousticness Levels Over Time --
-- Query: Calculate the average energy and acousticness for songs released each year. --

SELECT EXTRACT(YEAR FROM t.release_date) AS release_year, 
       AVG(ms.energy) AS avg_energy, 
       AVG(ms.acousticness) AS avg_acousticness
FROM track t
JOIN MusicalStats ms ON t.name = ms.track_name
GROUP BY release_year
ORDER BY release_year;
