# Exercise 1-07: Using entropy as a criterion

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

SEED = 1

df = pd.read_csv('input/wbc.csv')

y = df['diagnosis'].map({'M': 1, 'B': 0})
X = df.dropna(axis=1).drop(['id', 'diagnosis'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)

# Instantiate dt_entropy, set 'entropy' as the information criterion
dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)

# Fit dt_entropy to the training set
dt_entropy.fit(X_train, y_train)
