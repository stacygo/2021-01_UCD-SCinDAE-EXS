# Exercise 3-13: Writing an iterator to load data in chunks (3)

# The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use
import pandas as pd
import matplotlib.pyplot as plt

# Code from previous exercise
urb_pop_reader = pd.read_csv('input/world_ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'],
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(pop[0] * pop[1] * 0.01) for pop in pops_list]

print(df_pop_ceb.head())

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
