def find_bob(s):
    if len(s) < 3:
        return 0
    elif s[0:3] == 'bob':
        return 1 + find_bob(s[1:])
    else:
        return 0 + find_bob(s[1:])
