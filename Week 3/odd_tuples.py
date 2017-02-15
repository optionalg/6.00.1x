def oddTuples(aTup):
    if len(aTup) == 0:
        return ()
    elif len(aTup) < 3:
        return (aTup[0],)

    return (aTup[0],) + oddTuples(aTup[2:])
