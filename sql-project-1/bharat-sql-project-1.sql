-- In the ‘dsstudent’ database, create a permanent table named “customer_{your_name}.”
CREATE TABLE customer_bharat_kusuma
	(customer_id SMALLINT,
	name VARCHAR(20),
	location VARCHAR(20),
	total_expenditure VARCHAR(20),
	CONSTRAINT pk_customer PRIMARY KEY (customer_id)
	);

-- Insert the following records to the “customer_{your_name}” table:
INSERT INTO customer_bharat_kusuma 
	(customer_id, name, location, total_expenditure)
VALUES 
	(1701, "John", "Newport Beach, CA", 2000),
	(1707, "Tracy", "Irvine, CA", 1500),
	(1711, "Daniel", "Newport Beach, CA", 2500),
	(1703, "Ella", "Santa Ana, CA", 1800),
	(1708, "Mel", "Orange, CA", 1700),
	(1716, "Steve", "Irvine, CA", 18000);

-- Oops! The value in the field ”total_expenditure” of Steve is not correct. It should be “1800.” 
-- Can you update this record?
UPDATE customer_bharat_kusuma 
SET total_expenditure = 1800
WHERE name = "Steve";

-- We would like to update our customer data. Can you insert a new column called “gender” 
-- in the “customer_{your_name}” table?
-- The datatype of this column is “VARCHAR(20)”
ALTER TABLE customer_bharat_kusuma 
ADD gender VARCHAR(20);
 
-- Then, update the field “gender” with the following records:
UPDATE customer_bharat_kusuma 
SET gender = 'M'
WHERE name IN ('John', 'Daniel', 'Steve');

UPDATE customer_bharat_kusuma
SET gender = 'F'
WHERE name NOT IN ('John', 'Daniel', 'Steve');

-- The customer, Steve, decides to quit our membership program, 
-- so delete his record from the “customer_{your_name}” table.
DELETE FROM customer_bharat_kusuma
WHERE name = "Steve";

-- Add a new column called “store” in the table “customer_{your_name}”
ALTER TABLE customer_bharat_kusuma 
ADD store VARCHAR(20);

-- Then, delete the column called “store” in the table “customer_{your_name}” 
-- because you accidentally added it.
ALTER TABLE customer_bharat_kusuma
DROP COLUMN	store; 

-- Use “SELECT” & “FROM” to query the whole table “customer_{your_name}”
SELECT *
FROM customer_bharat_kusuma;

-- Return “name” and “total_expenditure” fields from the table “customer_{your_name}”
SELECT name, total_expenditure
FROM customer_bharat_kusuma;

-- Return “name” and “total_expenditure” fields from the table “customer_{your_name}” 
-- by using column alias (“AS” keyword)
SELECT name AS n, total_expenditure AS total_exp
FROM customer_bharat_kusuma;

-- Change the datatype of the field “total_expenditure” from “VARCHAR” to ”SMALLINT”
ALTER TABLE customer_bharat_kusuma
MODIFY total_expenditure SMALLINT;

-- Sort the field “total_expenditure” in descending order
SELECT total_expenditure
FROM customer_bharat_kusuma
ORDER BY total_expenditure DESC;

-- Return the top 3 customer names with the highest expenditure amount from the table 
-- “customer_{your_name}”
SELECT name, total_expenditure
FROM customer_bharat_kusuma
ORDER BY total_expenditure DESC
LIMIT 3;

-- Return the number of unique values of the field “location” and use the column alias to 
-- name the return field as “nuniques”
SELECT COUNT(DISTINCT(location)) AS nuniques
FROM customer_bharat_kusuma;

-- Return the unique values of the field “location” and use the column alias to name the return 
-- field as “unique_cities”
SELECT DISTINCT(location) AS unique_cities
FROM customer_bharat_kusuma;

-- Return the data where the gender is male.
SELECT *
FROM customer_bharat_kusuma
WHERE gender = "M";

-- Return the data where the gender is female.
SELECT *
FROM customer_bharat_kusuma
WHERE gender = "F";

-- Return the data where the location is “Irvine, CA”
SELECT *
FROM customer_bharat_kusuma
WHERE location = "Irvine, CA";
 
-- Return “name” and “location” where the ”total_expenditure” is less than 2000 and sort the result 
-- by the field “name” in ascending order
SELECT name, location
FROM customer_bharat_kusuma
WHERE total_expenditure < 2000
ORDER BY name ASC;

-- Drop the table “customer_{your_name}” after you finish all the questions.
DROP TABLE customer_bharat_kusuma;