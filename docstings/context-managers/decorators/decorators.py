
"""
You have written a decorator called print_args that prints out all of the arguments and their values any time a function that 
it is decorating gets called.
"""
def print_args(func):
    def print_vals(*args):
        print('{} was called with a={}, b={}, c={}'.format(func.__name__, args[0], args[1], args[2]))

    return print_vals

def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator

my_function = print_args(my_function)

my_function(1, 2, 3)


# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)
