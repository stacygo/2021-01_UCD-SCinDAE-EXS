# Exercise 2-06: Inconsistent categories

# The pandas package has been imported as pd, and the airlines DataFrame is in your environment.
import pandas as pd

airlines = pd.DataFrame({'id': [1351],
                         'day': ['Tuesday'],
                         'airline': ['UNITED INTL'],
                         'destination': ['KANSAI'],
                         'dest_region': ['Asia'],
                         'dest_size': ['Hub'],
                         'boarding_area': ['Gates 91-102'],
                         'dept_time': ['2018-12-31'],
                         'wait_min': [115.0],
                         'cleanliness': ['Clean'],
                         'safety': ['Neutral'],
                         'satisfaction': ['Very satisfied']})

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
