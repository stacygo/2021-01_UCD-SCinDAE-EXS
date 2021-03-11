# Exercise 4-06: Non-linear model of education

import pandas as pd
import statsmodels.formula.api as smf

gss = pd.read_hdf('input/gss.hdf5', 'gss')

gss['age2'] = gss['age']**2

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Print the estimated parameters
print(results.params)
