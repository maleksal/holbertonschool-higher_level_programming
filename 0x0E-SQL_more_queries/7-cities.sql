--  script that creates the database hbtn_0d_usa and the table cities
-- ENJOY!
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
