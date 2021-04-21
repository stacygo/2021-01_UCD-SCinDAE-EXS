# Exercise 3-05: Prepare the ground

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

SEED = 1

# Instantiate dt
dt = DecisionTreeClassifier(min_samples_leaf=8, random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, oob_score=True, random_state=SEED)
