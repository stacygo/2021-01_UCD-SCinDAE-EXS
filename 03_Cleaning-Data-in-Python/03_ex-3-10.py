# Exercise 3-10: Missing investors

# The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt respectively.
# # The banking DataFrame is in your environment.
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

banking = pd.DataFrame({'cust_id': ['8C35540A'],
                        'age': [54],
                        'acct_amount': [44244.7],
                        'inv_amount': [35500.5],
                        'account_opened': ['03-05-18'],
                        'last_transaction': ['30-09-19']})

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()
