def namelist(names):
    #your code here
    space = []
    for x in names[:-2]:
        x = list(x.values())
        for y in x:
            space.append(y)
            space.append(', ')
    for x in names[-2:-1]:
        x = list(x.values())
        for y in x:
            space.append(y)
            space.append(' & ')
    try:
        x = list(names[-1].values())
        for y in x:
            space.append(y)
    except IndexError:
        return ''
    return ''.join(space)
