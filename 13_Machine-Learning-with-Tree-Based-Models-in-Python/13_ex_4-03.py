# Exercise 4-03: Train the AdaBoost classifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

SEED = 1

df = pd.read_csv('input/indian_liver_patient/indian_liver_patient_preprocessed.csv')

y = df['Liver_disease']
X = df.drop(['Liver_disease'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

dt = DecisionTreeClassifier(max_depth=2, random_state=SEED)
ada = AdaBoostClassifier(base_estimator=dt, n_estimators=180, random_state=SEED)

# Fit ada to the training set
ada.fit(X_train, y_train)

# Compute the probabilities of obtaining the positive class
y_pred_proba = ada.predict_proba(X_test)[:, 1]
