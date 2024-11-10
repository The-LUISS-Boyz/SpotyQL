-- 5. Predicting Chart Success with Musical Attributes --
-- Query: Retrieve average values of danceability, energy, valence, and speechiness for songs in different chart ranges (e.g., top 10, 10-50, 50-100). --

SELECT chart_range,
       AVG(d) AS avg_danceability,
       AVG(e) AS avg_energy,
       AVG(v) AS avg_valence,
       AVG(s) AS avg_speechiness
FROM (
    SELECT CASE 
               WHEN tc.count <= 10 THEN 'Top 10'
               WHEN tc.count <= 50 THEN 'Top 10-50'
               WHEN tc.count <= 100 THEN 'Top 50-100'
               ELSE 'Below 100'
           END AS chart_range,
           ms.danceability AS d,
           ms.energy AS e,
           ms.valence AS v,
           ms.speechiness AS s,
           tc.count AS rank
    FROM track t
    JOIN MusicalStats ms ON t.id = ms.track_id
    JOIN Track_Chart tc ON t.id = tc.track_id
) AS subquery
GROUP BY chart_range
ORDER BY rank;
