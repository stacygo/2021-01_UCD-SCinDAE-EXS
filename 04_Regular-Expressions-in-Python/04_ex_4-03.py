# Exercise 4-03: Flying home

flight = "Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT"

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
print(flight_matches)

# Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))
