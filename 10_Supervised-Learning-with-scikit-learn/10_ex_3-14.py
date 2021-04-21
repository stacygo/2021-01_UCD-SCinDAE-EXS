# Exercise 3-14: Hold-out set in practice I: Classification

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('input/diabetes.csv')

imp = SimpleImputer(missing_values=0, strategy='mean')
imp.fit(df['insulin'].values.reshape(-1, 1))
df['insulin'] = imp.transform(df['insulin'].values.reshape(-1, 1))

imp.fit(df['bmi'].values.reshape(-1, 1))
df['bmi'] = imp.transform(df['bmi'].values.reshape(-1, 1))

imp.fit(df['triceps'].values.reshape(-1, 1))
df['triceps'] = imp.transform(df['triceps'].values.reshape(-1, 1))

y = df['diabetes']
X = df.drop('diabetes', axis=1)

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Create the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space, 'penalty': ['l1', 'l2']}

# Instantiate the logistic regression classifier: logreg
logreg = LogisticRegression(solver='liblinear', multi_class='ovr', n_jobs=1)

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the training data
logreg_cv.fit(X_train, y_train)

# Print the optimal parameters and best score
print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))
