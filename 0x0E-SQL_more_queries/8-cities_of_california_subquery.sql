-- script that lists all the cities of California.
-- ENJOY!
SELECT DISTINCT cities.id, cities.name FROM cities, states
WHERE state_id =(
	SELECT states.id FROM states
	WHERE name="California"
	)
ORDER BY cities.id ASC;
