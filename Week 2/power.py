"""
Iterative Power function
"""

def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    value = base
    iteration = 1

    if exp == 0:
        return 1

    while iteration < exp:
        value = value * base
        iteration += 1

    return value

def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recur_power(base, exp - 1)

print recur_power(5, 1)
print recur_power(5, 2)
print recur_power(5, 4)
print recur_power(5, 0)
