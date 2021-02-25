# Exercise 3-06: Putting the bike trips into the right time zone

import datetime

onebike_datetimes = [{'start': datetime.datetime(2017, 10, 1, 15, 23, 25),
                      'end': datetime.datetime(2017, 10, 1, 15, 26, 26)},
                     {'start': datetime.datetime(2017, 10, 1, 15, 42, 57),
                      'end': datetime.datetime(2017, 10, 1, 17, 49, 59)},
                     {'start': datetime.datetime(2017, 10, 2, 6, 37, 10),
                      'end': datetime.datetime(2017, 10, 2, 6, 42, 53)},
                     {'start': datetime.datetime(2017, 10, 2, 8, 56, 45),
                      'end': datetime.datetime(2017, 10, 2, 9, 18, 3)},
                     {'start': datetime.datetime(2017, 10, 2, 18, 23, 48),
                      'end': datetime.datetime(2017, 10, 2, 18, 45, 5)},
                     {'start': datetime.datetime(2017, 10, 2, 18, 48, 8),
                      'end': datetime.datetime(2017, 10, 2, 19, 10, 54)},
                     {'start': datetime.datetime(2017, 10, 2, 19, 18, 10),
                      'end': datetime.datetime(2017, 10, 2, 19, 31, 45)},
                     {'start': datetime.datetime(2017, 10, 2, 19, 37, 32),
                      'end': datetime.datetime(2017, 10, 2, 19, 46, 37)},
                     {'start': datetime.datetime(2017, 10, 3, 8, 24, 16),
                      'end': datetime.datetime(2017, 10, 3, 8, 32, 27)},
                     {'start': datetime.datetime(2017, 10, 3, 18, 17, 7),
                      'end': datetime.datetime(2017, 10, 3, 18, 27, 46)},
                     {'start': datetime.datetime(2017, 10, 3, 19, 24, 10),
                      'end': datetime.datetime(2017, 10, 3, 19, 52, 8)}]

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)
