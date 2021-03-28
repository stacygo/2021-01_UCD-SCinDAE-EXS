# Exercise 3-12: Writing an iterator to load data in chunks (2)

# You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas has been imported as pd
import pandas as pd

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('input/world_ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
