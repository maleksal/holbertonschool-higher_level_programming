-- lists all records with a score >= 10. table second_table of the database hbtn_0c_0
-- Enjoy it!
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
