# Permutation of a given string using inbuilt function

from itertools import permutations

def allPermutation(string):
    permList = permutations(string)

    for i in list(permList):
        print(''.join(i))

s = 'ABC'
allPermutation(s)