# Exercise 3-12: Finding ambiguous datetimes

import datetime
from dateutil import tz

onebike_datetimes = [{'start': datetime.datetime(2017, 10, 1, 15, 23, 25, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 1, 15, 26, 26, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 1, 15, 42, 57, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 1, 17, 49, 59, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 6, 37, 10, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 6, 42, 53, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 8, 56, 45, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 9, 18, 3, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 18, 23, 48, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 18, 45, 5, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 18, 48, 8, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 19, 10, 54, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 19, 18, 10, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 19, 31, 45, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 2, 19, 37, 32, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 2, 19, 46, 37, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 3, 8, 24, 16, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 3, 8, 32, 27, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 3, 18, 17, 7, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 3, 18, 27, 46, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime.datetime(2017, 10, 3, 19, 24, 10, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime.datetime(2017, 10, 3, 19, 52, 8, tzinfo=tz.gettz('US/Eastern'))}]

# Loop over trips
for trip in onebike_datetimes:
    # Rides with ambiguous start
    if tz.datetime_ambiguous(trip['start']):
        print("Ambiguous start at " + str(trip['start']))
    # Rides with ambiguous end
    if tz.datetime_ambiguous(trip['end']):
        print("Ambiguous end at " + str(trip['end']))
