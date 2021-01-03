# Ways to sort list of dictionaries by values in Python – Using itemgetter
# Advantages of itemgetter over lambda
# 1. Performance : itemgetter performs better than lambda functions in the context of time.
# 2. Concise : : itemgetter looks more concise when accessing multiple values than lambda functions.

'''
Itemgetter can be used instead of lambda function to achieve 
the similar functionality. Outputs in same way as sorted() and lambda,
but has different internal implementation. It takes keys of dictionaries
and converts them into tuples. It reduces overhead and is faster and 
more efficient. The “operator” module has to be imported for its working. 
The code is explained below
'''

from operator import itemgetter

# Initializing list of dictionaries 
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }]


print("====== using sorted + itemgetter ======")
print("List printed sorting by age")
print (sorted(lis, key=itemgetter('age')))
print("list printed sorting by age and name")
print(sorted(lis, key=itemgetter('age','name')))
print("The list printed sorting by age in descending order: ")
print(sorted(lis, key=itemgetter('age'), reverse=True))


print('\n====== using sorted + lambda function ======')
print("List printed sorting by age")
print(sorted(lis, key= lambda x : x['age']))
print("list printed sorting by age and name")
print(sorted(lis, key= lambda x : (x['age'], x['name']) ))
print("The list printed sorting by age in descending order: ")
print(sorted(lis , key= lambda x : x['age'], reverse= True))