def f(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}

    for key in d1.keys():
        if key in d2.keys():
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]

    for key in d2.keys():
        if key in d1.keys():
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d2[key]

    return (inter, diff)

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1, d2)
