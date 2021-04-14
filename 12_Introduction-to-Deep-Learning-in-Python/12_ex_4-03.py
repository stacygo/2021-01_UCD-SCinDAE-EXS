# Exercise 4-03: Changing optimization parameters

import pandas as pd
from tensorflow.keras.utils import to_categorical
from functions import get_new_model

df = pd.read_csv('input/titanic_all_numeric.csv')[:800]
df_test = pd.read_csv('input/titanic_all_numeric.csv')[801:]

target = to_categorical(df.survived)
predictors = df.drop(['survived'], axis=1).values

n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Import the SGD optimizer
from keras.optimizers import SGD

# Create list of learning rates: lr_to_test
lr_to_test = [.000001, 0.01, 1.]

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n' % lr)

    # Build new model to test, unaffected by previous models
    model = get_new_model(input_shape)

    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr=lr)

    # Compile the model
    model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')

    # Fit the model
    model.fit(predictors, target)
