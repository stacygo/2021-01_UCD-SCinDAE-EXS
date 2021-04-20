# Exercise 3-10: Closures keep your values safe (1)

# Show that you still get the original message even
# if you redefine my_special_function() to only print "hello".


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


new_func = get_new_func(my_special_function)


# Redefine my_special_function() to just print "hello"
def my_special_function():
    print('Hello')


new_func()
