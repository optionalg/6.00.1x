def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    result = []

    for element in aList:
        if isinstance(element, type([])):
            result = result + flatten(element)
        else:
            result.append(element)

    return result

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
