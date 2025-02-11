# %% [markdown]
# Read the json_file.txt file and print the values. The expected output should look like this: image
# 
# 

# %%
import pandas as pd

daily_covid_cases_txt = pd.read_json("json_file.txt")
print(daily_covid_cases_txt)

# %% [markdown]
# Read the daily_covid_cases.json file and print the values. The expected output should look like this: image

# %%
daily_covid_cases_json = pd.read_json("daily_covid_cases.json")
print(daily_covid_cases_json)

# %%



