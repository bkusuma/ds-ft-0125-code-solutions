# %%
import pandas as pd
import sqlite3

# %%
conn = sqlite3.connect("telecom.db") # connect to database

# %% [markdown]
# #1 Retrieve table names from the database (telecom.db).

# %%
q = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""
# display table names in database

pd.read_sql(q, conn)

# %% [markdown]
# #2 Join all tables in the database on the primary key.

# %%
q = """
SELECT t.id, t.location, t.fault_severity,
	et.event_type, st.severity_type,
	rt.resource_type, lf.log_feature, lf.volume 
FROM train t
	INNER JOIN event_type et
	ON t.id = et.id
	INNER JOIN severity_type st
	ON t.id = st.id
	INNER JOIN resource_type rt
	ON t.id = rt.id
	INNER JOIN log_feature lf
	ON t.id = lf.id;
"""
# join tables on id

pd.read_sql(q, conn)

# %% [markdown]
# #3 Find unique occurrences of event_type and severity in the table from #2 using an SQL query.

# %%
q = """
SELECT COUNT(DISTINCT(event_type)), COUNT(DISTINCT(severity_type))
FROM train t
	INNER JOIN event_type et
	ON t.id = et.id
	INNER JOIN severity_type st
	ON t.id = st.id
	INNER JOIN resource_type rt
	ON t.id = rt.id
	INNER JOIN log_feature lf
	ON t.id = lf.id;
"""
# count distinct event_type and severity_type in the table from #2

pd.read_sql(q, conn)

# %% [markdown]
# #4 Find how many occurrences there are of each fault_severity in the table from #2 using an SQL query.

# %%
q = """
SELECT fault_severity, COUNT(fault_severity)
FROM train t
	INNER JOIN event_type et
	ON t.id = et.id
	INNER JOIN severity_type st
	ON t.id = st.id
	INNER JOIN resource_type rt
	ON t.id = rt.id
	INNER JOIN log_feature lf
	ON t.id = lf.id
GROUP BY fault_severity;
"""
# count occurrences there are of each fault_severity in the table from #2

pd.read_sql(q, conn)


