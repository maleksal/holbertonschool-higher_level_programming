-- script that lists the number of records with the same score in the table second_table
-- Enjoy it!
SELECT score, COUNT(name) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
