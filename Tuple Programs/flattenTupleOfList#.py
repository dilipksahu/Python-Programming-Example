# Python – Flatten tuple of List to tuple

'''
Input : test_tuple = ([5], [6], [3], [8])
Output : (5, 6, 3, 8)
'''

test_tuple = ([5, 6], [6, 7, 8, 9], [3])

print('====== 1. tuple() + list() ======')
print(tuple(sum(test_tuple,[])))


print('\n===== 2. tuple() + itertools.chain.from_iterable() ======')
from itertools import chain
res = tuple(chain.from_iterable(test_tuple))
print(res)