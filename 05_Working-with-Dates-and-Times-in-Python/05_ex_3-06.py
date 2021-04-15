# Exercise 3-06: Putting the bike trips into the right time zone

import pandas as pd

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})

onebike_datetimes = df[['start', 'end']].to_dict('records')

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)
