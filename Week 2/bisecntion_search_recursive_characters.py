def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return aStr == char

    half = len(aStr) // 2
    half_char = aStr[half]

    if half_char == char:
        return True
    elif half_char > char:
        return isIn(char, aStr[0:half])
    else:
        return isIn(char, aStr[half:])

print isIn('a', 'abc')
print isIn('b', 'abc')
print isIn('d', 'abcde')
