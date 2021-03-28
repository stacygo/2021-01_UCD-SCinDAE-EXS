# Exercise 3-10: Follow the money

import pandas as pd

banking = pd.read_csv('input/banking_dirty.csv')
banking.loc[banking['age'] < 29, 'cust_id'] = None
banking.loc[banking['age'] < 30, 'acct_amount'] = None

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())
