# Exercise 5-08: Set the hyperparameter grid of RF

# Define the dictionary 'params_rf'
params_rf = {'n_estimators': [100, 350, 500],
             'min_samples_leaf': [2, 10, 30],
             'max_features': ['log2', 'auto', 'sqrt']}
