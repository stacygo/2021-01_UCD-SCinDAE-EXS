# Exercise 4-06: Define the GB regressor

from sklearn.ensemble import GradientBoostingRegressor

SEED = 2

# Instantiate gb
gb = GradientBoostingRegressor(max_depth=4, n_estimators=200, random_state=SEED)
