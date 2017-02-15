"""
The greatest common divisor of two positive integers is the largest
integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1
"""

def gcd_iter(num_1, num_2):
    '''
    num_1, num_2: positive integers
    returns: a positive integer, the greatest common divisor of num_1 & num_2.
    '''
    if num_1 < num_2:
        gcd = num_1
    else:
        gcd = num_2
    while gcd > 1:
        if (num_1 % gcd == 0) and (num_2 % gcd == 0):
            return gcd
        else:
            gcd -= 1
    return gcd

def gcd_recur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)

print gcd_recur(2, 12)
print gcd_recur(6, 12)
print gcd_recur(9, 12)
print gcd_recur(17, 12)
