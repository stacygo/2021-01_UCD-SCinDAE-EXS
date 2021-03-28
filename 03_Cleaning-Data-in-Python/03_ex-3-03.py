# Exercise 3-03: Uniform currencies

# The pandas package has been imported as pd, and the banking DataFrame is in your environment.
import pandas as pd

banking = pd.read_csv('input/banking_dirty.csv', nrows=97)
banking['acct_cur'] = pd.read_csv('input/banking_dirty_acct_cur.csv', header=None)

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'
