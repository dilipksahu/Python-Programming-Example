# Extract Unique values dictionary values

print("======= Using sorted() + set comprehension + values() ======")

test_dict = {'gfg' : [5, 6, 7, 8], 
             'is' : [10, 11, 7, 5], 
             'best' : [6, 12, 10, 8], 
             'for' : [1, 2, 5]} 
# Using set comprehension + values() + sorted() 
res = list(sorted({ ele for val in test_dict.values() for ele in val }))

print("The unique values in list: " + str(res))
  

print("=====  Using chain() + sorted() + values() ======")
from itertools import chain

result = list(set(chain(*test_dict.values())))

print("The unique values in list: " ,result)