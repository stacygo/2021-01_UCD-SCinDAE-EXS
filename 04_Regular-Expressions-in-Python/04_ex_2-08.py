# Exercise 2-08: On time

import datetime

east = {'date': datetime.datetime(2007, 4, 20, 0, 0), 'price': 1232443}
west = {'date': datetime.datetime(2006, 5, 26, 0, 0), 'price': 1432673}

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")
