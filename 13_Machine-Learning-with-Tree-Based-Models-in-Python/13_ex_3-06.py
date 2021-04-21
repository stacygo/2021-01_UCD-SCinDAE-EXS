# Exercise 3-06: OOB Score vs Test Set Score

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

SEED = 1

df = pd.read_csv('input/indian_liver_patient/indian_liver_patient_preprocessed.csv')

y = df['Liver_disease']
X = df.drop(['Liver_disease'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

dt = DecisionTreeClassifier(min_samples_leaf=8, random_state=SEED)
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, oob_score=True, random_state=SEED)

# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate test set accuracy
acc_test = accuracy_score(y_test, y_pred)

# Evaluate OOB accuracy
acc_oob = bc.oob_score_

# Print acc_test and acc_oob
print('Test set accuracy: {:.3f}, OOB accuracy: {:.3f}'.format(acc_test, acc_oob))
