# Exercise 2-09: Removing titles and taking names

# The airlines DataFrame is in your environment, alongside pandas as pd.
import pandas as pd

airlines = pd.read_csv('input/airlines_final.csv', nrows=200)
airlines['full_name'] = pd.read_csv('input/airlines_final_full_name.csv', header=None)

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")

# Assert that full_name has no honorifics
assert not airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any()
