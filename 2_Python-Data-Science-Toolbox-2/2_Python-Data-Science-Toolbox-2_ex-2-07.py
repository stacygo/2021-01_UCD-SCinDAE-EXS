# Exercise 2-07: Using conditionals in comprehensions (1)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) > 6]

# Print the new list
print(new_fellowship)