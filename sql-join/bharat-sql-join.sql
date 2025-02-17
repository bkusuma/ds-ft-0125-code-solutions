-- Write a SQL query to left outer join all the tables in the telecom database.
-- Note: Only ”id”, “location”, “fault_severity”, “event_type”, “severity_type”,
--  “resource_type”, “log_feature”, “volume” columns will be included.

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