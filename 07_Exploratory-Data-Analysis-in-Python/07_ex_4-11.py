# Exercise 4-11: Predicting a binary variable

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

gss['age2'] = gss['age']**2
gss['educ2'] = gss['educ']**2

# Recode grass
gss['grass'].replace(2, 0, inplace=True)

formula = 'grass ~ age + age2 + educ + educ2 + C(sex)'

# Run logistic regression
results = smf.logit(formula, data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

plt.clf()
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label='Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()
