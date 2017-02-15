def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    difference = num - 1
    exponent = 0
    done = False

    while not done:
        new_exponent = exponent + 1
        new_difference = abs(num - (base**new_exponent))

        if new_difference < difference:
            difference = new_difference
            exponent = new_exponent
        else:
            done = True

    return exponent

print closest_power(3, 12)
print closest_power(4, 12)
print closest_power(4, 1)
