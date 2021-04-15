# Exercise 3-12: Finding ambiguous datetimes

import pandas as pd
from dateutil import tz

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})
df['start'] = df['start'].dt.tz_localize('America/New_York', ambiguous=True)
df['end'] = df['end'].dt.tz_localize('America/New_York', ambiguous=True)

onebike_datetimes = df[['start', 'end']].to_dict('records')

# Loop over trips
for trip in onebike_datetimes:
    # Rides with ambiguous start
    if tz.datetime_ambiguous(trip['start']):
        print("Ambiguous start at " + str(trip['start']))
    # Rides with ambiguous end
    if tz.datetime_ambiguous(trip['end']):
        print("Ambiguous end at " + str(trip['end']))
