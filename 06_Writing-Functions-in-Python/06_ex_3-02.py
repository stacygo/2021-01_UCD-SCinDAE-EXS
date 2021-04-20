# Exercise 3-02: Building a command line data app

from functions import mean, std, minimum, maximum, load_data, get_user_input

# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}


data = load_data()
print(data)

# Note: The function get_user_input() in this exercise is a mock version of asking the user
# to enter a command. It randomly returns one of the four function names.
# In real life, you would ask for input and wait until the user entered a value.
func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)
