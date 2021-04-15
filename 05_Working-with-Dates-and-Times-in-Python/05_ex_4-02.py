# Exercise 4-02: Loading a csv file in Pandas

# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])
