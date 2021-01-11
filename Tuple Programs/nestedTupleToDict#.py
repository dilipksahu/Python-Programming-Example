# Python – Convert Nested Tuple to Custom Key Dictionary

'''
Input : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’, ‘value’, ‘id’]
Output : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]
'''

test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

print('====== 1. list comp + dict ======')
res = [ {'key':sub[0],'value':sub[1],'id':sub[2]} for sub in test_tuple]
print(res)


print('\n====== 2. zip() + list comp =======')
keys = ['key','value','id']
output1 = [ dict(zip(keys,sub)) for sub in test_tuple]
output2 = [ { key:val for key, val in zip(keys,sub)} for sub in test_tuple]
print(output1)
print(output2)