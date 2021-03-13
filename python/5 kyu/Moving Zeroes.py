def move_zeros(array):
    #your code here
    name = []
    zeroes = 0
    for i in array:
        if i != 0 or type(i) == bool or None:
            name.append(i)
        else:
            zeroes += 1
    for i in range(zeroes):
        name.append(0)
    return name
