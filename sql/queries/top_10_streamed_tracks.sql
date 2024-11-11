-- Top 10 Most Streamed Tracks --
-- Lists the top 10 tracks by total stream count in descending order. --

SELECT name, streams FROM Track ORDER BY streams DESC LIMIT 10;
