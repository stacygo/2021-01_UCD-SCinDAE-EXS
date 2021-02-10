# Exercise 3-07: How's our data integrity?

# Both pandas and datetime have been imported as pd and dt respectively.
import pandas as pd
import datetime as dt

banking = pd.DataFrame({'cust_id': ['8C35540A'],
                        'birth_date': ['1962-06-09 00:00:00'],
                        'age': [59],
                        'acct_amount': [63523.3],
                        'inv_amount': [51295],
                        'fund_A': [30105.0],
                        'fund_B': [4138.0],
                        'fund_C': [1420.0],
                        'fund_D': [15632.0],
                        'account_opened': ['02-09-18'],
                        'last_transaction': ['22-02-19']})

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

# Store today's date and find ages
today = dt.date.today()
banking['birth_date'] = pd.to_datetime(banking['birth_date'])
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])
