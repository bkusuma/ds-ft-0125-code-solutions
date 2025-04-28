# SELECT/FROM/AS
-- Write a SQL query to return “id”, “log_feature” and “volume” from “log_feature” table by using “table alias” and “column alias.” 
-- (Note: You don’t need to use column alias on column "id".)
SELECT id, l.log_feature 'log', l.volume 'vol'
FROM log_feature l;

# Sorting
-- Write a SQL query to return the first 5 rows of “id”, “resource_type” and sorted by ”id” column and "resource_type" column in ascending order.
SELECT id, rt.resource_type
FROM resource_type rt 
ORDER BY id DESC, resource_type ASC 
LIMIT 5;

-- Write a SQL query to return the last 5 rows of “id”, “resource_type” and sorted by ”id” column in descending order.
SELECT id, resource_type
FROM(
	SELECT id, resource_type
	FROM resource_type
	ORDER BY id ASC
	) as temporary_table
ORDER BY id DESC
LIMIT 5;

-- Write a SQL query to return 5 rows of “id”, “resource_type” and sorted by ”id” column in ascending order first, then sorted by “resource_type” column in a descending order.
SELECT id, rt.resource_type
FROM resource_type rt 
ORDER BY id ASC, resource_type DESC 
LIMIT 5;

# Count/distinct
-- Write a SQL query to return the following data from severity_type:
-- Numbers of rows
-- Numbers of unique values of column ‘id’
-- Numbers of unique values of column ‘severity_type’
SELECT COUNT(*) 'numbers_row', COUNT(DISTINCT(id)) 'id_nunique', COUNT(DISTINCT(severity_type)) 'severity_type_nunique'
FROM severity_type;

# WHERE filtering
-- Write a SQL query to return from the “log_feature” table, ”feature_201” with a volume between 100 and 300.
-- In the query result, return ‘id’, ‘log_feature’, ‘volume’ columns only
-- Sort the result by the ‘volume’ column
SELECT id, log_feature, volume
FROM log_feature lf
WHERE lf.log_feature = 'feature 201'
	AND volume BETWEEN 100 AND 300
ORDER BY volume ASC;