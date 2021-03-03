# Exercise 3-04: Returning functions for a math game


def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b

        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b

        return subtract
    else:
        print("I don't know that one")


add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
