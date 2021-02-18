# Exercise 3-04: Uniform dates

# The banking DataFrame is in your environment and pandas was imported as pd.
import pandas as pd

banking = pd.DataFrame({'cust_id': ['8C35540A'],
                        'acct_amount': [44244.7],
                        'acct_cur': ['dollar'],
                        'inv_amount': [35500.5],
                        'account_opened': ['2018-03-05'],
                        'last_transaction': ['30-09-19']})

# Print the header of account_opened
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format=True,
                                           # Return missing value for error
                                           errors='coerce')

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])
