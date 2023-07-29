-- Assuming the table name is "work_data"
SELECT
    bot_id AS "Bot ID",
    MIN(timestamp) AS "Work Start",
    MAX(timestamp) AS "Work End",
    ARRAY_AGG(activity) AS "Activities"
FROM
    work_data
GROUP BY
    bot_id, FLOOR(EXTRACT(epoch FROM timestamp) / (5 * 60))  -- Grouping by 5-minute intervals
ORDER BY
    bot_id, "Work Start";
