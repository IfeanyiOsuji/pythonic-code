
"""
You have written a decorator called print_args that prints out all of the arguments and their values any time a function that 
it is decorating gets called.
"""
def print_args(func):
    def print_vals(*args):
        print('{} was called with a={}, b={}, c={}'.format(func.__name__, args[0], args[1], args[2]))
        func(*args)

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


"""
Print the return type

You are debugging a package that you've been working on with your 
friends. Something weird is happening with the data being returned 
from one of your functions, but you're not even sure which function is
 causing the trouble. You know that sometimes bugs can sneak into your 
 code when you are expecting a function to return one thing, and it returns 
 something different. For instance, if you expect a function to return a 
 numpy array, but it returns a list, you can get unexpected behavior. 
 To ensure this is not what is causing the trouble, you decide to write 
 a decorator, print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.



    Create a nested function, wrapper(), that will become the new decorated function.
    Call the function being decorated.
    Return the new decorated function.

"""

def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, *kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))





"""
Counter

You're working on a new web app, and you are curious about how many times 
each of the functions in it gets called. So you decide to write a decorator 
that adds a counter to each function that you decorate. You could use this 
information in the future to determine whether there are sections of code that 
you could remove because they are no longer being used by the app.


    Call the function being decorated and return the result.
    Return the new decorated function.
    Decorate foo() with the counter() decorator.

"""

def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, *kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

"""
It seems a little magical that you can reference the wrapper() function 
from _inside_ the definition of wrapper() as we do here on line 3. That's just 
one of the many neat things about functions in Python -- any function, not just decorators.
"""





"""
Preserving docstrings when decorating functions

Your friend has come to you with a problem. They've written some nifty 
decorators and added them to the functions in the open-source library they've
 been working on. However, they were running some tests and discovered that all 
 of the docstrings have mysteriously disappeared from their decorated functions.
   Show your friend how to preserve docstrings and other metadata when writing decorators.


"""

# Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function

from functools import wraps # used to preserve the metadata of the decorated function

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)



"""
HTML Generator

You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators 
that will add bold or italics tags to any function that returns a string. You notice, however, 
that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators,
 you want to create one decorator, html(), that can take any pair of opening and closing tags.

def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper

def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper

"""

# Return the decorator and the decorated function from the correct places in the new html() decorator.

def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator


# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
  return 'Hello {}!'.format(name)
  
print(hello('Alice'))

# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
  return 'Goodbye {}.'.format(name)
  
print(goodbye('Alice'))


# Use html() to wrap hello_goodbye() in a DIV, which is done by adding the strings <div> and </div> tags around a string.
# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
  return '\n{}\n{}\n'.format(hello(name), goodbye(name))
  
print(hello_goodbye('Alice'))
