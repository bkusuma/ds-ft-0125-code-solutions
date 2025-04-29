# %%
import pandas as pd
import sqlite3

# %%
conn = sqlite3.connect("hr.db") # connect to database

# %% [markdown]
# Retrieve table names from the database (hr.db).

# %%
q = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""
# create query to find tables in database

pd.read_sql(q, conn)

# %% [markdown]
# Retrieve EmployeeNumber, Department, Age, Gender, and Attrition for employees in sales department from the Employee table; save that information into a dataframe named ‘sales’.

# %%
q = """
SELECT *
FROM employee;
"""
# create query to find features of employee table

pd.read_sql(q, conn)

# %%
q = """
SELECT EmployeeNumber, Department, Age, Gender, Attrition
FROM employee;
"""
# retrieve requested table data

sales = pd.read_sql(q, conn)
sales
# save as dataframe named "sales"

# %% [markdown]
# Retrieve EmployeeNumber, EducationField, Age, Gender, and Attrition for employees in the Life Sciences field from the Employee table, save that information into a dataframe named ‘field’.

# %%
q = """
SELECT EmployeeNumber, EducationField, Age, Gender, Attrition
FROM employee
WHERE EducationField = "Life Sciences";
"""
# retrieve requested table data

field = pd.read_sql(q, conn)
field
# save as dataframe named "field"

# %% [markdown]
# Save the two dataframes as tables in the database, and then join the tables on the primary key.

# %%
sales.to_sql("sales", conn)

# %%
field.to_sql("field", conn)

# %%
q = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""
# check that new tables are in database

pd.read_sql(q, conn)

# %%
q = """
SELECT *
FROM sales s
INNER JOIN field f
ON s.EmployeeNumber = f.EmployeeNumber;
"""
# join tables on primary key EmployeeNumber

pd.read_sql(q, conn)


