# Exercise 3-10: Closures keep your values safe (3)

# Show that you still get the original message even
# if you overwrite my_special_function() with the new function.


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()
