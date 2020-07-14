-- script that creates the database hbtn_0d_2 and the user user_0d_2
-- Enjoy it!

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user with username & password
CREATE USER IF NOT EXISTS user_0d_2@localhost
	IDENTIFIED BY 'user_0d_2_pwd';

-- give select privileges to user
GRANT SELECT
	ON hbtn_0d_2.*
	TO user_0d_2@localhost;
