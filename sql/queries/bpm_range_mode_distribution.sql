-- Distribution of Tracks by BPM Ranges and Mode --
-- Groups tracks by BPM ranges and mode, then counts tracks in each group. --

SELECT
  CASE WHEN bpm BETWEEN 60 AND 80 THEN '60-80'
       WHEN bpm BETWEEN 81 AND 100 THEN '81-100'
       ELSE '101+'
  END AS bpm_range,
  mode,
  COUNT(*) AS track_count
FROM MusicalStats
GROUP BY bpm_range, mode;
