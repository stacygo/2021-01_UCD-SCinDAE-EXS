# Exercise 3-10: Follow the money

import pandas as pd

banking = pd.DataFrame({'cust_id': ['8C35540A'],
                        'age': [54],
                        'acct_amount': [44244.7],
                        'inv_amount': [35500.5],
                        'account_opened': ['03-05-18'],
                        'last_transaction': ['30-09-19']})

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())