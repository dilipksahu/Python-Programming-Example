# Python – Order Tuples by List

'''
Input : test_list = [(‘Gfg’, 10), (‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)], ord_list = [‘Geeks’, ‘best’, ‘CS’, ‘Gfg’]
Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)]
'''
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)] 
ord_list = ['Geeks', 'best', 'CS', 'Gfg'] 

print('====== using dict() + list comp =======')
temp = dict(test_list)
res = [ (key, temp[key]) for key in ord_list]
print(ord_list)
print(res)



print('\n====== setdefault() + sorted() + lambda ======')
temp = dict()
for key, ele in enumerate(ord_list):
    # dictionary.setdefault(keyname, value)
    temp.setdefault(ele,[]).append(key)
print(temp)

# sort test_list based on temp keys ordered
output = sorted(test_list, key= lambda ele : temp[ele[0]].pop() )
print(output)

