# Exercise 1-09: Using * and zip to 'unzip'

# Two tuples of strings, mutants and powers have been pre-loaded
mutants = ('charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde')
powers = ('telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility')

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)