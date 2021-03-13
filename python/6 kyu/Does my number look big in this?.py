def narcissistic( value ):
    # Code away
    return True if sum(int(char)**len(str(value)) for char in [int(x) for x in str(value)]) == value else False
