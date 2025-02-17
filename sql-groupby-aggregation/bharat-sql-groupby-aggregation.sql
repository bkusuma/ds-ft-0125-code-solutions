-- NOTE: Use the query from the sql-join assignment to create a temporary table 
-- to be used for the first two problems.
CREATE TEMPORARY TABLE dsstudent.bharat_sql_join
	(id SMALLINT, location VARCHAR(20), fault_severity SMALLINT,
	event_type VARCHAR(20), severity_type  VARCHAR(20), resource_type VARCHAR(20),
	log_feature VARCHAR(20), volume SMALLINT);
	
INSERT INTO dsstudent.bharat_sql_join
	(id, location, fault_severity,
	event_type, severity_type, resource_type,
	log_feature, volume)
	SELECT t.id, t.location, t.fault_severity,
	et.event_type, st.severity_type,
	rt.resource_type, lf.log_feature, lf.volume 
	FROM train t
	LEFT JOIN event_type et
	ON t.id = et.id
	LEFT JOIN severity_type st
	ON t.id = st.id
	LEFT JOIN resource_type rt
	ON t.id = rt.id
	LEFT JOIN log_feature lf
	ON t.id = lf.id;
 
# Write SQL statements to return data of the following questions:
-- For each location, what is the quantity of unique event types?
SELECT location, COUNT(DISTINCT(event_type)) num_unique_event_type
FROM dsstudent.bharat_sql_join
GROUP BY location;

-- What are the top 3 locations with the most volumes?
SELECT location, SUM(volume) total_volume
FROM dsstudent.bharat_sql_join
GROUP BY location
ORDER BY total_volume DESC
LIMIT 3;

# Write SQL statements to return data of the following questions:
-- For each fault severity, what is the quantity of unique locations?
SELECT fault_severity, COUNT(DISTINCT(location)) num_of_unique_locations
FROM dsstudent.bharat_sql_join
GROUP BY fault_severity;

-- From the query result above, what is the quantity of unique locations 
-- with the fault_severity greater than 1?
SELECT fault_severity, COUNT(DISTINCT(location)) num_of_unique_locations
FROM dsstudent.bharat_sql_join
GROUP BY fault_severity
HAVING fault_severity > 1;

# Write a SQL query to return the minimum, maximum, average 
-- of the field “Age” for each “Attrition” groups from the “hr” database.

SELECT Attrition, MIN(Age) min_age, MAX(Age) max_age, AVG(Age) avg_age
FROM hr.employee
GROUP BY Attrition;

# Write a SQL query to return the “Attrition”, “Department” 
-- and the number of records from the ”hr” database for each group in the 
-- “Attrition” and “Department.” Sort the returned table by the “Attrition” and 
-- “Department” fields in ascending order.
SELECT Attrition, Department, COUNT(Department) num_quantity
FROM hr.employee
WHERE Attrition IS NOT NULL
GROUP BY Attrition, Department 
ORDER BY Attrition ASC, Department ASC;

# From Question #4, can you return the results where the “num_quantity” is greater than 100 records?
## hold my beer
SELECT Attrition, Department, COUNT(Department) num_quantity
FROM hr.employee
WHERE Attrition IS NOT NULL
GROUP BY Attrition, Department
HAVING num_quantity > 100
ORDER BY Attrition ASC, Department ASC;

