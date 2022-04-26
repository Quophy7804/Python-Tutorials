"""
Parameter and Arguments
----------------
what if we want the function to print a statement anytime it runs?

parameters goes inside the parathensis when a function is defined
"""

def example_function(message):
    print(message) #this was the message parameter will be printed out to the console

''' now we just pass whatever string we want the message to be in the parathensis 
when calling the function thus making it the argument
'''
example_function("Hi")

example_function("This is Bill")

"""
NOTE: we have multiple parameters

def example_function(message, number):
    print(message) 
    print(number)
    
example_function("How many?", 5)

"""