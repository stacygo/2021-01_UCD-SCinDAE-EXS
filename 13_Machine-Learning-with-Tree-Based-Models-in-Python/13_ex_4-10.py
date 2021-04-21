# Exercise 4-10: Regression with SGB

from sklearn.ensemble import GradientBoostingRegressor

SEED = 2

# Instantiate sgbr
sgbr = GradientBoostingRegressor(max_depth=4, subsample=0.9, max_features=0.75, n_estimators=200,
                                 random_state=SEED)
