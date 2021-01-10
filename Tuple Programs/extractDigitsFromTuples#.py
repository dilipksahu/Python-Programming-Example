# Python – Extract digits from Tuple list

'''
Input : test_list = [(15, 3), (3, 9)]
Output : [9, 5, 3, 1]
'''

test_list = [(15,3), (3, 9), (1, 10), (99, 2)] 

print('======= using itertools.chain.from_iterable =======')
from itertools import chain
# output : [15, 3, 3, 9, 1, 10, 99, 2]
flatten_list = chain.from_iterable(test_list)

res = []
for ele in flatten_list:
    for digit in str(ele):
        res.append(int(digit))

print(list(set(res)))


print('\n===== re.sub() =======')
import re
# output: 15339110992
flat_list = re.sub(r'[\[\]\(\), ]','',str(test_list))
result = [ int(digit)  for digit in str(flat_list)]

print(list(set(result)))



### Note:
# itertools.chain example
'''
from_iterable = chain.from_iterable(['geeks',  
                                     'for', 
                                     'geeks', 
                                     ['w', 'i', 'n', 's']])

output : [‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’, ‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘w’, ‘i’, ‘n’, ‘s’]
'''