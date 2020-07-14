--  script that creates the table unique_id
-- Enjoy it!
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
