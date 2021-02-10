# Exercise 2-10: Keeping it descriptive

# The airlines DataFrame is in your environment, and pandas is imported as pd.
import pandas as pd

airlines = pd.DataFrame({'id': [2913],
                         'day': ['Friday'],
                         'airline': ['TURKISH AIRLINES'],
                         'destination': ['ISTANBUL'],
                         'dest_region': ['Middle East'],
                         'dest_size': ['Hub'],
                         'boarding_area': ['Gates 91-102'],
                         'dept_time': ['2018-12-31'],
                         'wait_min': [225.0],
                         'cleanliness': ['Dirty'],
                         'safety': ['Very unsafe'],
                         'satisfaction': ['Very unsatisfied'],
                         'survey_response': ['The airport personnell forgot to alert us of delayed flights, the bathrooms could have been cleaner']})

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])
