# %%
import pandas as pd
import sqlite3

# %%
conn = sqlite3.connect("stocks.sqlite") # connect to database

# %%
q = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""
# create query to find tables in database

pd.read_sql(q, conn)

# %%
q_STOCK_DATA = """
SELECT *
FROM STOCK_DATA;
"""
# reading STOCK_DATA table

pd.read_sql(q_STOCK_DATA, conn)

# %%
# find data types to create new table
pd.read_sql(q_STOCK_DATA, conn).info()

# %% [markdown]
# # Create two new tables in the database (stocks.sqlite), one with only 'MSFT' values for the Symbol feature, and one with only 'AAPL' values for the Symbol feature.

# %%
q_MSFT_TABLE = """
CREATE TABLE MSFT_TABLE
	('index' INT, Date TEXT, Open REAL, High REAL, Low REAL, Close REAL, Volume INT, 'Adj Close' REAL, Symbol VARCHAR(20));
"""
# create empty table for MSFT data

pd.read_sql(q_MSFT_TABLE, conn)

# Alternate execution method 1:
# with conn:
# 	conn.execute(q_MSFT_TABLE)

# Alternate execution method 2:
# cur = conn.cursor()
# cur.execute(q_MSFT_TABLE)

# %%
q_MSFT_INSERT = """
INSERT INTO MSFT_TABLE
	('index', Date, Open, High, Low, Close, Volume, 'Adj Close', Symbol)
SELECT *
	FROM STOCK_DATA
	WHERE Symbol = 'MSFT';
"""
# insert MSFT values into table

pd.read_sql(q_MSFT_INSERT, conn)

# Alternate method:
# CREATE TABLE MSFT_TABLE AS
# SELECT *
# FROM STOCK_DATA
# WHERE Symbol = 'MSFT';

# %%
q_AAPL_TABLE = """
CREATE TABLE AAPL_TABLE
	('index' INT, Date TEXT, Open REAL, High REAL, Low REAL, Close REAL, Volume INT, 'Adj Close' REAL, Symbol VARCHAR(20))
"""
# create empty table for AAPL data

pd.read_sql_query(q_AAPL_TABLE, conn)

# %%
q_AAPL_INSERT = """
INSERT INTO AAPL_TABLE
	('index', Date, Open, High, Low, Close, Volume, 'Adj Close', Symbol)
SELECT *
	FROM STOCK_DATA
	WHERE Symbol = 'AAPL';
"""
# insert AAPL values into table

pd.read_sql(q_AAPL_INSERT, conn)

# %% [markdown]
# # Read the two new new tables in from the database using SQL to check if they were successfully created.

# %%
q_MSFT_SHOW = """
SELECT *
FROM MSFT_TABLE;
"""
# show MSFT_TABLE

pd.read_sql(q_MSFT_SHOW, conn)

# %%
q_AAPL_SHOW = """
SELECT *
FROM AAPL_TABLE;
"""
# show AAPL_TABLE

pd.read_sql(q_AAPL_SHOW, conn)

# %% [markdown]
# # For each new table in the database, query for rows containing the Maximum and Minimum dates, and save those rows as new pandas data frames (2 rows per dataframe).

# %%
q_MSFT_DATES = """
SELECT MAX(Date), MIN(Date)
FROM MSFT_TABLE;
"""
# show MSFT_TABLE Maximum and Minimum dates

df_MSFT_DATES = pd.read_sql(q_MSFT_DATES, conn).T
df_MSFT_DATES

# %%
q_AAPL_DATES = """
SELECT MAX(Date), MIN(Date)
FROM AAPL_TABLE;
"""
# show AAPL_TABLE Maximum and Minimum dates

df_AAPL_DATES = pd.read_sql(q_AAPL_DATES, conn).T
df_AAPL_DATES

# %% [markdown]
# # For each new table in the database, query for values greater than 50 in the Open feature, and save those as new pandas data frames.

# %%
q_MSFT_OPEN50 = """
SELECT *
FROM MSFT_TABLE
WHERE Open > 50;
"""
# MSFT_TABLE query for values greater than 50 in the Open feature

df_MSFT_OPEN50 = pd.read_sql(q_MSFT_OPEN50, conn)
df_MSFT_OPEN50

# %%
q_AAPL_OPEN50 = """
SELECT *
FROM AAPL_TABLE
WHERE Open > 50;
"""
# AAPL_TABLE query for values greater than 50 in the Open feature

df_AAPL_OPEN50 = pd.read_sql(q_AAPL_OPEN50, conn)
df_AAPL_OPEN50


