# %%
import requests
import pandas as pd

# %%
base_url = "https://api.themoviedb.org" # TMDb api site
with open("/Users/bharat/Documents/Data Science/LearningFuze VS Code/api_keys/TMDbAPIKey.txt", "r") as file: # load API key
        api_key = file.read() # set API key as variable
query_string = "star%20wars" # string to query from API
page = 1 # default page of results
api_url = f"/3/search/movie?api_key={api_key}&query={query_string}&page={page}" # resolved API URL part

full_url = base_url + api_url # constructing full URL to call
results = requests.get(full_url) # results from API
results_json = results.json() # convert to JSON

all_results = [] # create empty list to grab results from all pages

for page in range(1, results_json['total_pages'] + 1): # cycle through pages and get results from each page
        page = page
        full_url = base_url + api_url
        results = requests.get(full_url)
        page_results = results.json()
        page_result_list = page_results['results']
        all_results.extend(page_result_list) # extend list with each list of results on each page
        
star_wars_df = pd.DataFrame(all_results) # format the JSON object into a DataFrame

star_wars_df

# %%
star_wars_df.sort_values(by="popularity",ascending=False) # sort the movies in the DataFrame by popularity (highest to lowest)


