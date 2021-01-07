# Keys associated with Values in Dictionary

'''
Input : test_dict = {‘gfg’ : [1, 2, 3], ‘is’ : [1, 4], ‘best’ : [4, 2]}
Output : {1: [‘is’, ‘gfg’], 2: [‘gfg’, ‘best’], 3: [‘gfg’], 4: [‘is’, ‘best’]
'''
print('======= Naive Method ======')
def keyAssociation(input):
    dic = {}
    for key, value in input.items():
        for i in value:
            if i in dic:
                dic[i].append(key)
            else:
                dic[i] = []
                dic[i].append(key)
    print(dic)

test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}
keyAssociation(test_dict)



print('\n====== defaultdict() ========')
from collections import defaultdict
def keyAssdefaultdict(input):
    dic = defaultdict(list)
    for key , val in input.items():
        for ele in val:
            dic[ele].append(key)
    print(dic)

keyAssdefaultdict(test_dict)