# Exercise 3-08: Look before you leap: EDA before hypothesis testing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_ID = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
         'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
         'B', 'B', 'B', 'B']

df_impact = [1.612, 0.605, 0.327, 0.946, 0.541, 1.539, 0.529, 0.628, 1.453, 0.297, 0.703, 0.269,
             0.751, 0.245, 1.182, 0.515, 0.435, 0.383, 0.457, 0.73, 0.172, 0.142, 0.037, 0.453,
             0.355, 0.022, 0.502, 0.273, 0.72, 0.582, 0.198, 0.198, 0.597, 0.516, 0.815, 0.402,
             0.605, 0.711, 0.614, 0.468]

df = pd.DataFrame(data={'ID': df_ID, 'impact_force': df_impact})

# Make bee swarm plot
_ = sns.swarmplot(x='ID', y='impact_force', data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()

