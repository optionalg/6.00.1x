def reverse(L):
    '''
        L: a list
        Returns the list in the inverse order
    '''
    L_copy = L[:]
    length = len(L)

    for i in range(length):
        L[i] = L_copy[length-i-1]

def deep_reverse(L):
    '''
    L: a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    '''
    length = len(L)

    for i in range(length):
        reverse(L[i])

    reverse(L)

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print L
