import string

def is_pangram(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    y = True
    for i in str(alphabet):
        if i in str(x).lower():
            y = y
        else:
            y = False
    return y
