"""
Sum of the area and perimeter^2 of a polygon
"""
from math import tan, pi

def polysum(n, s):
    """
    n_sides: number of sides
    s_length: lenght of each side
    Returns the sum of the area and square of the perimeter
    of the regular polygon rounded to 4 decimal places
    """
    area = (0.25 * n * (s**2))/tan(pi/n)
    perimeter = n * s
    return round(area + (perimeter**2), 4)
