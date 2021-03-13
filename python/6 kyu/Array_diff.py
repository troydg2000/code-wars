def array_diff(a, b):
    #your code here
    diff = []
    for i in a:
        if i not in b:
            diff.append(i)
        else:
            continue
    if len(a)==0:
        diff = []
    else:
        diff = diff
    return diff
