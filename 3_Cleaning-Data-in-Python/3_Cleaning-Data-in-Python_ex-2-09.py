# Exercise 2-09: Removing titles and taking names

# The airlines DataFrame is in your environment, alongside pandas as pd.
import pandas as pd

airlines = pd.DataFrame({'id': [1351],
                         'full_name': ['Melodie Stuart'],
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

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")

# Assert that full_name has no honorifics
assert not airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any()
