# Python – Join Tuples if similar initial element

'''
Input : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
'''

test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] 

print('======= 1. Using loop =======')
res = []
for sub in test_list:
    # check for empty res if no then check for last item and compare with first item of tuples
    if res and res[-1][0] == sub[0]:
        res[-1].extend(sub[1:])
    else:
        # if res is empty add one item first
        res.append( [ele for ele in sub ])

# convert list items into tuple by map function
print(list(map(tuple,res)))


print('\n====== defaultdict and loop =======')
from collections import defaultdict
mapp = defaultdict(list)
for key , val in test_list:
    # output : defaultdict(<class 'list'>, {5: [6, 7], 6: [8, 10], 7: [13]})
    mapp[key].append(val)

res = [ (k,*v) for k, v in mapp.items() ]
print(res)