# Exercise 3-02: Define the bagging classifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

SEED = 1

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=SEED)
