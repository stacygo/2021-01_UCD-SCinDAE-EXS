# Exercise 1-03: Retrieving docstrings

import inspect
from functions import count_letter, build_tooltip

# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

# Get the docstring with a function from the inspect module
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
