# Table creation/insertion
-- Create a permanent table called ‘person_{your_name}’ in the “dsstudent” database. This table has 4 columns, ‘person_id’, 
-- ‘first_name’, ‘last_name’, ‘city’ (‘person_id’ is the primary key).
CREATE TABLE person_bharat_kusuma
	(person_id SMALLINT,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	city VARCHAR(20),
	CONSTRAINT pk_person PRIMARY KEY (person_id)
	);

-- Insert a row of data into this table.
INSERT INTO person_bharat_kusuma
	(person_id, first_name, last_name, city)
VALUES 
	(1, 'Bharat', "Kusuma", 'Cypress');

-- Insert 2 rows of data into this table
INSERT INTO person_bharat_kusuma
	(person_id, first_name, last_name, city)
VALUES 
	(2, 'JJ', 'Abrams', "Los Angeles"),
	(3, "Sarah", 'Smile', 'Chicago');

# Update data in table
-- Add a new column called ‘gender’ in the ‘person_{your_name}’ table.
ALTER TABLE person_bharat_kusuma
ADD gender CHAR(1);

-- Update data to this column.
UPDATE person_bharat_kusuma
SET gender = 'M'
WHERE person_id = 1 OR 2;

UPDATE person_bharat_kusuma
SET gender = 'F'
WHERE person_id = 3;

# Delete data/drop table
-- Delete the column ‘gender’ from the ‘person_{your_name}’ table.
ALTER TABLE person_bharat_kusuma
DROP COLUMN	gender; 

-- Delete the row where ‘personal_id = 2’ from the ‘person_{your_name}’ table.
DELETE FROM person_bharat_kusuma
WHERE person_id = 2;

-- Drop the ‘person_{your_name}’ table from the ’dsstudent’ database.
DROP TABLE person_bharat_kusuma;
