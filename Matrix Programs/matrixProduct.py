# Matrix Product for 2D 

print("======== for loop and list comp =======")
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]] 
res = prod( [ ele for sub in test_list for ele in sub ])
print(res)


print("======== itertoos.chain() ============")
from itertools import chain

def prodMatrix(val):
    res = 1
    for ele in val:
        res *= ele
    return res

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]] 
result = prod(list(chain(*test_list)))
print(result)
