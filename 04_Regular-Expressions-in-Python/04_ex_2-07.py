# Exercise 2-07: Make this function

number1 = 120
number2 = 7
string1 = "httpswww.datacamp.com"
list_links = ['www.news.com', 'www.google.com', 'www.yahoo.com', 'www.bbc.com', 'www.msn.com', 'www.facebook.com', 'www.news.google.com']

# Include both variables and the result of dividing them
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1 / number2:0.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links) * 100 / 120:0.2f}% of the posts contain links")