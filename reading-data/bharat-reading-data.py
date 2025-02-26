# %% [markdown]
# # Exercise
# Read the data from the file into a DataFrame.
# 
# Save the data from the DataFrame into file with a different name than the original file, but with the same data format.
# 
# Re-read the file to ensure it saved properly.

# %%
import pandas as pd

# %% [markdown]
# # mtcars.csv

# %%
cars = pd.read_csv("mtcars.csv") # open .csv file as data frame
cars.head()

# %%
cars.to_csv("mtcars_copy.csv", index=False)

# %% [markdown]
# # u.data 

# %%
u_data = pd.read_table("u.data") # read table to become a data frame
u_data.head()

# %%
u_data.to_csv("COPY - u.data", index=False)

# %% [markdown]
# # beer.txt 

# %%
beer = pd.read_csv("beer.txt", sep = " ") # read .txt file and delimit by using space separator to become a data frame
beer.head()

# %%
beer.to_csv("beer_copy.txt", index=False)

# %% [markdown]
# # u.item

# %%
u_item = pd.read_table("u.item", sep="|", encoding="latin-1", header=None) # open file with "|" separator to become a data frame
u_item.head()

# %%
u_item.to_csv("COPY - u.item", sep="|", index=False)

# %% [markdown]
# # NHL 2015-16.xlsx

# %%
hockey = pd.read_excel("NHL 2015-16.xlsx")
hockey.head()

# %%
hockey.to_excel("COPY - NHL 2015-16.xlsx", index=False)

# %%
# Name: open_file
# Purpose: function that would read all the previous file types without exceptions
# Inputs:   1. take one file name as a string
# Outputs:  1. DataFrame of file data
# Side effects: none

def open_file(file_name):
    file_type = file_name.rsplit(".", 1)[1]
    if file_type == "xlsx": # open Excel files as above
        df = pd.read_excel(file_name)
    elif file_type == "csv": # open CSV files as above
        df = pd.read_csv(file_name)
    else: # open other files
        delimiter = input("What is the delimiter used in this data?\nPress Enter if N/A") # ask user for delimiter used in data
        if delimiter == "":
            delimiter = None # set to default if nothing entered
        encoder = input("What is the encoder used in this data?\nPress Enter if N/A") # ask user for delimiter used in data
        if encoder == "":
            encoder = None # set to default if nothing entered
        df = pd.read_table(file_name, sep=delimiter, encoding=encoder) # open file user inputted delimiter and encoder
    return df

open_file("mtcars.csv")

# %%



