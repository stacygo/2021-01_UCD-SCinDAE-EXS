# Exercise 3-07: What time did the bike leave? (Global edition)

import datetime
from dateutil import tz

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

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())
