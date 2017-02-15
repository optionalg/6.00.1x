def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    Returns the dot products of two vectors
    '''
    total = 0
    length = len(listA)

    for i in range(length):
        total += (listA[i] * listB[i])

    return total

print dotProduct([1, 2, 3], [4, 5, 6])
