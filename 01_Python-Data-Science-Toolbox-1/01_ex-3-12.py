# Exercise 3-12: Bringing it all together (1)

import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)