# learning about functions
# what are functions in programming?
# functions are a block of reusable that only runs whens it is called.
# you can pass data known as parameters or arguments, into a funtion.A function can return data as a result.
# function help to organize and modurelize code.

# how to define a  functiom in python
# in python, a function is defined using the "def" keyword
def my_function():
    print("hello from a funtion")

# How to call function in python 
# To call a function in python, use the funtion name followed by parenthesis:
my_function()

def greetings(user_name):
    return(f"hello(user_name)")

print(greetings("John"))

# calculate the area of a circle

import math

def circle_area(radius):
    return math.pi * radius ** 2 # the foemula is usualy pi * r ** 2

print(circle_area(5))

# not using math module
def circle_area(radius):
    return 3.142 * radius ** 2

print(circle_area(7))
