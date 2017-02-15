"""
Sample functions
"""

def square(number):
    """
    x: int or float
    Return square of x
    """
    return number * number

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return (a * (x * x)) + (b * x) + c

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2 == 1
