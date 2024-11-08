-- 4. Analyzing Year-over-Year Growth in Popularity --
-- Query: Compute the year-over-year growth in streams (percentage change in streams from the previous year) --

WITH YearlyStreams AS (
    SELECT 
        EXTRACT(YEAR FROM t.release_date) AS release_year, 
        SUM(t.streams) AS total_streams
    FROM track t
    GROUP BY release_year
)
SELECT 
    release_year,
    total_streams,
    LAG(total_streams) OVER (ORDER BY release_year) AS prev_year_streams,
    ((total_streams - LAG(total_streams) OVER (ORDER BY release_year)) 
     / NULLIF(LAG(total_streams) OVER (ORDER BY release_year), 0)) * 100 AS year_over_year_growth
FROM YearlyStreams
ORDER BY release_year;