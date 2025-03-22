# %%
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup as beautify
from io import StringIO

# %% [markdown]
# ## Connect to the web server and make sure you receive an ‘ok’ status code.

# %%
url = "https://www.formula1.com/en/results/2022/drivers"
website = requests.get(url)
website.status_code

# %% [markdown]
# ## Scrape the page for the statistics stored in the table.

# %%
site_soup = beautify(website.content)

table_list = site_soup.find_all("table")
table_list

# %% [markdown]
# ## Save the table as a data frame.

# %%
df = pd.read_html(StringIO(str(table_list)))
df = df[0]
df

# %% [markdown]
# ## Save the data frame as a .csv file, and re-read the file to make sure it saved correctly.

# %%
df.to_csv("2022DriverStandings.csv")

pd.read_csv("2022DriverStandings.csv")

# %% [markdown]
# ## Scrape the page using the pd.read_html( ) method.

# %%
pd.read_html("https://www.formula1.com/en/results/2022/drivers")


