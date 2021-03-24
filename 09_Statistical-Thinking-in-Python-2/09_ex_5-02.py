# Exercise 5-02: EDA of beak depths of Darwin's finches

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_depth = [8.4, 8.8, 8.4, 8., 7.9, 8.9, 8.6, 8.5, 8.9, 9.1, 8.6, 9.8, 8.2, 9., 9.7, 8.6, 8.2,
            9., 8.4, 8.6, 8.9, 9.1, 8.3, 8.7, 9.6, 8.5, 9.1, 9., 9.2, 9.9, 8.6, 9.2, 8.4, 8.9,
            8.5, 10.4, 9.6, 9.1, 9.3, 9.3, 8.8, 8.3, 8.8, 9.1, 10.1, 8.9, 9.2, 8.5, 10.2, 10.1,
            9.2, 9.7, 9.1, 8.5, 8.2, 9., 9.3, 8., 9.1, 8.1, 8.3, 8.7, 8.8, 8.6, 8.7, 8., 8.8,
            9., 9.1, 9.74, 9.1, 9.8, 10.4, 8.3, 9.44, 9.04, 9., 9.05, 9.65, 9.45, 8.65, 9.45,
            9.45, 9.05, 8.75, 9.45, 8.35, 9.4, 8.9, 9.5, 11., 8.7, 8.4, 9.1, 8.7, 10.2, 9.6,
            8.85, 8.8, 9.5, 9.2, 9., 9.8, 9.3, 9., 10.2, 7.7, 9., 9.5, 9.4, 8., 8.9, 9.4, 9.5,
            8., 10., 8.95, 8.2, 8.8, 9.2, 9.4, 9.5, 8.1, 9.5, 8.4, 9.3, 9.3, 9.6, 9.2, 10., 8.9,
            10.5, 8.9, 8.6, 8.8, 9.15, 9.5, 9.1, 10.2, 8.4, 10., 10.2, 9.3, 10.8, 8.3, 7.8, 9.8,
            7.9, 8.9, 7.7, 8.9, 9.4, 9.4, 8.5, 8.5, 9.6, 10.2, 8.8, 9.5, 9.3, 9., 9.2, 8.7, 9.,
            9.1, 8.7, 9.4, 9.8, 8.6, 10.6, 9., 9.5, 8.1, 9.3, 9.6, 8.5, 8.2, 8., 9.5, 9.7, 9.9,
            9.1, 9.5, 9.8, 8.4, 8.3, 9.6, 9.4, 10., 8.9, 9.1, 9.8, 9.3, 9.9, 8.9, 8.5, 10.6, 9.3,
            8.9, 8.9, 9.7, 9.8, 10.5, 8.4, 10., 9., 8.7, 8.8, 8.4, 9.3, 9.8, 8.9, 9.8, 9.1]

df_year = [1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975, 1975,
           1975, 1975, 1975, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012, 2012,
           2012, 2012, 2012, 2012]

df = pd.DataFrame(data={'beak_depth': df_depth, 'year': df_year})

# Create bee swarm plot
_ = sns.swarmplot(x='year', y='beak_depth', data=df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()
