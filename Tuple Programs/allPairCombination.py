# Python – All pair combinations of 2 tuples

'''
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
'''

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)

print('====== List comp + concatination(+)')
res = [ (i,j) for i in test_tuple1 for j in test_tuple2]
print(res + [(i,j) for i in test_tuple2 for j in test_tuple1 ])



print('===== Using chain() + product() =====')
from itertools import chain, product

result = list(chain(product(test_tuple1,test_tuple2),product(test_tuple2,test_tuple1)))
print(result)