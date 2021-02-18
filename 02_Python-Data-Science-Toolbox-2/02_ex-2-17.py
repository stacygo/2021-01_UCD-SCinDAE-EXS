# Exercise 2-17: Conditional list comprehensions for time-stamped data

# The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use
import pandas as pd
df = pd.read_csv('tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)