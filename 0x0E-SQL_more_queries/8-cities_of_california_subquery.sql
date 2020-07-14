-- script that lists all the cities of California.
-- ENJOY!
SELECT name FROM cities
WHERE id =(
	SELECT id FROM states
	WHERE name="California"
	);
