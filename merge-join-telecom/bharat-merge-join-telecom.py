# %% [markdown]
# # Merge Tables.

# %%
import pandas as pd

folder_path = "/Users/bharat/Documents/Data Science/LearningFuze VS Code/Homework/merge-join-telecom/Telstra Competition Data/"

train = pd.read_csv(folder_path + "train.csv")
severity_type = pd.read_csv(folder_path + "severity_type.csv")
event_type = pd.read_csv(folder_path + "event_type.csv")
log_feature = pd.read_csv(folder_path + "log_feature.csv")
resource_type = pd.read_csv(folder_path + "resource_type.csv")

train_merge = train.copy()

merge_dataframe_list = [severity_type, event_type, log_feature, resource_type]
for table in merge_dataframe_list:
    train_merge = train_merge.merge(table, on="id")

train_merge

# %% [markdown]
# 
# 
# | Explain the difference between inner and outer merge   | Explain the difference between merge and join |
# |--------------------------------------------------------|-------------------------------------------------|
#  Inner merge gets data indexed by primary keys that exist in both tables whereas outer merges get data indexed by primary keys that exist in either table | Join joins columns of another DataFrame whereas merge merges DataFrames with a database-style join.                                          

# %% [markdown]
# # Divide dataset into two dataframes.

# %%
top = train_merge.shape[0]//2
bottom = train_merge.shape[0] - top

top_half = train_merge.head(top)
bottom_half = train_merge.tail(bottom)

print(top_half.shape)
print(bottom_half.shape)

# %% [markdown]
# # Concat the two dataframes.

# %%
pd.concat([top_half, bottom_half])

# %% [markdown]
# # Handle duplicates.

# %%
train_merge.duplicated().sum()

# %% [markdown]
# ## note: no duplicates in data frame


