# Exercise 1-06: Extract a function

import pandas as pd
import json
from functions import standardize

with open('input/yearly_gpas.txt') as f:
    df = pd.DataFrame.from_dict(json.loads(f.read()))

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df['y1_gpa'])
df['y2_z'] = standardize(df['y2_gpa'])
df['y3_z'] = standardize(df['y3_gpa'])
df['y4_z'] = standardize(df['y4_gpa'])
