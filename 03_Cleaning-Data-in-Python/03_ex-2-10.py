# Exercise 2-10: Keeping it descriptive

# The airlines DataFrame is in your environment, and pandas is imported as pd.
import pandas as pd

airlines = pd.read_csv('input/airlines_final.csv', nrows=29)
airlines['survey_response'] = pd.read_csv('input/airlines_final_survey_response.csv', header=None, sep='\n')

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])
