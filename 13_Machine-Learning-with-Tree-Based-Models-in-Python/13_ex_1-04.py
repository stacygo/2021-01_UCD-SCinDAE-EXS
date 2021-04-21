# Exercise 1-04: Logistic regression vs classification tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from functions import plot_labeled_decision_regions
from sklearn.linear_model import LogisticRegression

SEED = 1

df = pd.read_csv('input/wbc.csv')

y = df['diagnosis'].map({'M': 1, 'B': 0})
X = df[['radius_mean', 'concave points_mean']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)

dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)
dt.fit(X_train, y_train)

# Instatiate logreg
logreg = LogisticRegression(random_state=SEED)

# Fit logreg to the training set
logreg.fit(X_train, y_train)

# Define a list called clfs containing the two classifiers logreg and dt
clfs = [logreg, dt]

# Review the decision regions of the two classifiers
plot_labeled_decision_regions(X_test, y_test, clfs)
