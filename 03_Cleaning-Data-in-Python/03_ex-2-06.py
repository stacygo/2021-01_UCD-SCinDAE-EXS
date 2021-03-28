# Exercise 2-06: Inconsistent categories

# The pandas package has been imported as pd, and the airlines DataFrame is in your environment.
import pandas as pd

airlines = pd.read_csv('input/airlines_final.csv')

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
