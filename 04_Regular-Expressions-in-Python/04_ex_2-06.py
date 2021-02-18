# Exercise 2-06: Literally formatting

field1 = "sexiest job"
field2 = "data is produced daily"
field3 = "Individuals"
fact1 = 21
fact2 = 2500000000000000000
fact3 = 72.41415415151
fact4 = 1.09

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1}st century")

# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")
