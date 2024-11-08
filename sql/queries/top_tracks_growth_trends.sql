-- 11. Comprehensive Analysis of Top 5 Tracks and Their Growth Trends --
-- The query identifies the top 5 tracks by total streams, analyzes their platform presence --
-- (Spotify, Apple Music, Deezer, Shazam), examines their musical attributes (danceability, energy, etc.), --
-- and calculates their year-over-year growth in streams, providing insights into the correlation between --
-- streaming popularity and musical characteristics across different platforms and time. --

WITH YearlyStreams AS (
    SELECT 
        EXTRACT(YEAR FROM t.release_date) AS release_year, 
        SUM(t.streams) AS total_streams
    FROM track t
    GROUP BY release_year
),
TrackDetails AS (
    SELECT 
        t.name AS track_name,
        t.streams AS total_streams,
        t.in_spotify_playlists,
        t.in_spotify_charts,
        t.in_apple_playlists,
        t.in_apple_charts,
        t.in_deezer_playlists,
        t.in_deezer_charts,
        t.in_shazam_charts,
        ms.danceability AS danceability,
        ms.energy AS energy,
        ms.valence AS valence,
        ms.bpm AS bpm,
        ms.acousticness AS acousticness,
        ms.instrumentalness AS instrumentalness,
        ms.liveness AS liveness
    FROM track t
    JOIN MusicalStats ms ON t.name = ms.track_name
),
YearlyGrowth AS (
    SELECT 
        release_year,
        total_streams,
        LAG(total_streams) OVER (ORDER BY release_year) AS prev_year_streams,
        ((total_streams - LAG(total_streams) OVER (ORDER BY release_year)) 
         / NULLIF(LAG(total_streams) OVER (ORDER BY release_year), 0)) * 100 AS year_over_year_growth
    FROM YearlyStreams
)
SELECT 
    td.track_name,
    td.total_streams,
    td.in_spotify_playlists,
    td.in_spotify_charts,
    td.in_apple_playlists,
    td.in_apple_charts,
    td.in_deezer_playlists,
    td.in_deezer_charts,
    td.in_shazam_charts,
    td.danceability,
    td.energy,
    td.valence,
    td.bpm,
    td.acousticness,
    td.instrumentalness,
    td.liveness,
    yg.release_year,
    yg.year_over_year_growth
FROM TrackDetails td
JOIN YearlyGrowth yg ON EXTRACT(YEAR FROM td.release_year) = yg.release_year
ORDER BY td.total_streams DESC
LIMIT 5;
