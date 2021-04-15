# Exercise 3-03: Setting timezones

import pandas as pd

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})

onebike_datetimes = df[['start', 'end']].to_dict('records')

# Import datetime, timezone
from datetime import timedelta, timezone

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=edt)
    trip['end'] = trip['end'].replace(tzinfo=edt)
