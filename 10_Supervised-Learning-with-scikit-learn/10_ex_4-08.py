# Exercise 4-08: Imputing missing data in a ML Pipeline II

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv('input/house-votes-84.csv')
df[df == '?'] = 'NaN'
df[df == 'y'] = 1
df[df == 'n'] = 0

y = df['party']
X = df.drop(['party'], axis=1)

# Import necessary modules
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Setup the pipeline steps: steps
steps = [('imputation', SimpleImputer(missing_values='NaN', strategy='most_frequent')),
        ('SVM', SVC())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
