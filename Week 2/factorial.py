"""
factorial
"""

def factorial(number):
    """
    Returns the factorial of a number
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print factorial(5)
