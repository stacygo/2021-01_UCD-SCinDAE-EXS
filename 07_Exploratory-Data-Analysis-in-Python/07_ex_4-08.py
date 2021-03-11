# Exercise 4-08: Making predictions

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

gss = pd.read_hdf('input/gss.hdf5', 'gss')

gss['age2'] = gss['age']**2
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0, 20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())
