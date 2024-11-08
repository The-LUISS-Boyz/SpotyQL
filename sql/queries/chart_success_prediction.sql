-- 5. Predicting Chart Success with Musical Attributes --
-- Query: Retrieve average values of danceability, energy, valence, and speechiness for songs in different chart ranges (e.g., top 10, 10-50, 50-100). --

SELECT CASE 
           WHEN RANK() OVER (ORDER BY t.streams DESC) <= 10 THEN 'Top 10'
           WHEN RANK() OVER (ORDER BY t.streams DESC) <= 50 THEN 'Top 10-50'
           WHEN RANK() OVER (ORDER BY t.streams DESC) <= 100 THEN 'Top 50-100'
           ELSE 'Below 100'
       END AS chart_range,
       AVG(ms.danceability) AS avg_danceability,
       AVG(ms.energy) AS avg_energy,
       AVG(ms.valence) AS avg_valence,
       AVG(ms.speechiness) AS avg_speechiness
FROM track t
JOIN MusicalStats ms ON t.name = ms.track_name
GROUP BY chart_range
ORDER BY chart_range;
