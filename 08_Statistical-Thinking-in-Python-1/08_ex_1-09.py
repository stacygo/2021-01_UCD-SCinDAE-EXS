# Exercise 1-09: Bee swarm plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_petal_length = [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5, 1.6, 1.4, 1.1, 1.2, 1.5,
                   1.3, 1.4, 1.7, 1.5, 1.7, 1.5, 1., 1.7, 1.9, 1.6, 1.6, 1.5, 1.4, 1.6, 1.6, 1.5,
                   1.5, 1.4, 1.5, 1.2, 1.3, 1.4, 1.3, 1.5, 1.3, 1.3, 1.3, 1.6, 1.9, 1.4, 1.6, 1.4,
                   1.5, 1.4, 4.7, 4.5, 4.9, 4., 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4., 4.7,
                   3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4, 4.8, 5., 4.5, 3.5,
                   3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1, 4., 4.4, 4.6, 4., 3.3, 4.2, 4.2,
                   4.2, 4.3, 3., 4.1, 6., 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1, 5.1, 5.3,
                   5.5, 5., 5.1, 5.3, 5.5, 6.7, 6.9, 5., 5.7, 4.9, 6.7, 4.9, 5.7, 6., 4.8, 4.9, 5.6,
                   5.8, 6.1, 6.4, 5.6, 5.1, 5.6, 6.1, 5.6, 5.5, 4.8, 5.4, 5.6, 5.1, 5.1, 5.9, 5.7,
                   5.2, 5., 5.2, 5.4, 5.1]

df_species = ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
              'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
              'versicolor', 'versicolor', 'versicolor', 'versicolor', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
              'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica']

df = pd.DataFrame({'petal length (cm)': df_petal_length, 'species': df_species})

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
