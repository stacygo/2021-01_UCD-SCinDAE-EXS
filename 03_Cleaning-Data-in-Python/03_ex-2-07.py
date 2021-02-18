# Exercise 2-07: Remapping categories

# The pandas and numpy packages have been imported as pd and np. Let's create some new categorical data!
import pandas as pd
import numpy as np

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

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins=label_ranges, labels=label_names)

# Create mappings and replace
mappings = {'Monday': 'weekday', 'Tuesday': 'weekday', 'Wednesday': 'weekday',
            'Thursday': 'weekday', 'Friday': 'weekday',
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)
