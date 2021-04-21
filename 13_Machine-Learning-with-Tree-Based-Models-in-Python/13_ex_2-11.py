# Exercise 2-11: Evaluate individual classifiers

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

SEED = 1

df = pd.read_csv('input/indian_liver_patient/indian_liver_patient_preprocessed.csv')

y = df['Liver_disease']
X = df.drop(['Liver_disease'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

classifiers = [('Logistic Regression', LogisticRegression(C=1.0, class_weight=None, dual=False,
                                                          fit_intercept=True, intercept_scaling=1,
                                                          max_iter=100, multi_class='ovr', n_jobs=1,
                                                          penalty='l2', random_state=1,
                                                          solver='liblinear', tol=0.0001, verbose=0,
                                                          warm_start=False)),
               ('K Nearest Neighbours', KNeighborsClassifier(algorithm='auto', leaf_size=30,
                                                             metric='minkowski', metric_params=None,
                                                             n_jobs=1, n_neighbors=27, p=2,
                                                             weights='uniform')),
               ('Classification Tree', DecisionTreeClassifier(class_weight=None, criterion='gini',
                                                              max_depth=None, max_features=None,
                                                              max_leaf_nodes=None,
                                                              min_impurity_decrease=0.0,
                                                              min_impurity_split=None,
                                                              min_samples_leaf=0.13, min_samples_split=2,
                                                              min_weight_fraction_leaf=0.0,
                                                              random_state=1, splitter='best'))]

# Iterate over the pre-defined list of classifiers
for clf_name, clf in classifiers:
    # Fit clf to the training set
    clf.fit(X_train, y_train)

    # Predict y_pred
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Evaluate clf's accuracy on the test set
    print('{:s} : {:.3f}'.format(clf_name, accuracy))
