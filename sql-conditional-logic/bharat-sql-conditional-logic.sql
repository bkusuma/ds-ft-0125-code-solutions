# Write SQL statements to return data of the following questions:
-- In the log_feature table, write the conditional logic with the following conditions:
	-- If the volume < 100, then make those records as “low”
	-- If the volume between 100 and 500, then make those records as “medium”
	-- If the volume > 500, then make those records as ”large”
SELECT *,
	CASE
		WHEN volume < 100 THEN 'low'
		WHEN volume BETWEEN 100 and 500 THEN 'medium'
		WHEN volume > 500 THEN 'large'
	END volume_1
FROM log_feature;

-- From the query above, can you show the quantity of records for each “low”, “medium” and “large”?
## hell yeah I can just watch me
SELECT DISTINCT(volume_1), COUNT(volume) as value_counts
FROM (SELECT *,
		CASE
			WHEN volume < 100 THEN 'low'
			WHEN volume BETWEEN 100 and 500 THEN 'medium'
			WHEN volume > 500 THEN 'large'
		END volume_1
	FROM log_feature) as temporary_table
GROUP BY temporary_table.volume_1;

# Write a conditional logic with the following conditions:
-- If “HourlyRate” is greater and equal than 80, then make the records as “high hourly rate”
-- If “HourlyRate” is between 40 and 80, then make the records as “medium hourly rate”
-- If “HourlyRate” is less than 40, then make the records as “low hourly rate”
-- Return the “EmployeeNumber”, “HourlyRate”, and the conditional logic result in the end
SELECT EmployeeNumber, HourlyRate,
	CASE
		WHEN HourlyRate >= 80 THEN 'high hourly rate'
		WHEN HourlyRate >= 40 AND HourlyRate < 80 THEN 'medium hourly rate'
		WHEN HourlyRate < 40 THEN 'low hourly rate'
	END as HourlyRate_1
FROM hr.employee;

# Write a conditional logic with the following conditions:
-- If “Gender” is “Female”, then make the records as an integer “0”
-- If “Gender” is “Male”, then make the records as an integer “1”
-- Return the “Gender” and the conditional logic result in the end
SELECT Gender,
	CASE
		WHEN Gender = 'Female' THEN 0
		WHEN Gender = 'Male' THEN 1		
	END as Gender_1
FROM hr.employee;