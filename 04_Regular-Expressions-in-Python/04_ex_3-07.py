# Exercise 3-07: Some time ago

import pandas as pd
import re

sentiment_analysis_dict = {'232': "I would like to apologize for the repeated Video Games Live related tweets. 32 minutes ago",
                           '233': "@zaydia but i cant figure out how to get there / back / pay for a hotel 1st May 2019",
                           '234': "FML: So much for seniority, bc of technological ineptness 23rd June 2018 17:54"}

sentiment_analysis = pd.Series(data=sentiment_analysis_dict, index=['232', '233', '234'])

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))