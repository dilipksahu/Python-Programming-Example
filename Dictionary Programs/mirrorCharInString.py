# Python Dictionary to find mirror characters in a string

'''
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.
'''

def mirrorChar(input, K):
    # create dictionary 
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChar = dict(zip(original,reverse))

    prefix = input[0: K-1]
    suffix = input[K-1:]

    mirror = ''
    for i in range(0,len(suffix)):
        mirror = mirror + dictChar[suffix[i]]

    print(prefix + mirror)

input = "paradox"
N = 3
mirrorChar(input, N)