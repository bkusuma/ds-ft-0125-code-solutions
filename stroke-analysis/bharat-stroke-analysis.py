# %% [markdown]
# # Use .describe() to compute a variety of statistics on the whole data set at once.

# %%
import pandas as pd

stroke_data = pd.read_csv("healthcare-dataset-stroke-data.csv")
stroke_data.describe()

# %% [markdown]
# 
# # Filter .describe() to only compute statistics on factors with floating point number values.
# 

# %%
stroke_data.describe(include=float)

# %% [markdown]
# 
# # Use .groupby() to create a data frame grouping by the "stroke" factor.

# %%
grouped = stroke_data.groupby("stroke")
grouped

# %% [markdown]
# 
# # Use the "stroke" grouping to get only group where "stroke" is 1.
# 

# %%
stroke_group = grouped.get_group(1) # alternately can filter data e.g. stroke_data[stroke_data["stroke"] == 1]
stroke_group

# %% [markdown]
# 
# # Use .describe() to compute statistics on factors with floating point values for the data where "stroke" is 1.
# 

# %%
stroke_group.describe(include=float)

# %% [markdown]
# 
# # Filter .describe() to only compute statistics on factors with integer values, removing as much percentile data as possible.
# 

# %%
stroke_group.describe(include=int,percentiles=[])

# %% [markdown]
# 
# # Create a data frame grouping by both the "hypertension" and "heart_disease" factors.
# 

# %%
hyper_heart = stroke_data.groupby(["hypertension", "heart_disease"])
hyper_heart

# %% [markdown]
# 
# # Get the group where both "hypertension" and "heart_disease" are 1.
# 

# %%
hyper_heart.get_group((1,1))

# %% [markdown]
# 
# # Count the number of "id"s per group.
# 

# %%
hyper_heart.get_group((1,1)).count().loc["id"]

# %% [markdown]
# 
# # Aggregate both the mean and standard deviation of "stroke" per group.

# %%
stroke_mean = hyper_heart.get_group((1,1))["stroke"].mean()
stroke_std = hyper_heart.get_group((1,1))["stroke"].std()

print(f"The mean is {stroke_mean} and the standard deviation is {stroke_std}.")


