# Exercise 2-08: Using conditionals in comprehensions (2)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) > 6 else '' for member in fellowship]

# Print the new list
print(new_fellowship)
