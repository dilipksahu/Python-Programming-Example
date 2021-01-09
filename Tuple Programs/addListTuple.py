# Adding Tuple to List and vice – versa

test_list = [5, 6, 7] 
test_tup = (9, 10)

print('===== Adding Tuple to List  ====')
print('===== Using += operator (list + tuple) ======')
# This operator can be used to join a list with a tuple. 
# Internally its working is similar to that of list.extend(), 
# which can have any iterable as its argument, tuple in this case.

test_list += test_tup
print(test_list)


print('===== Adding List to Tuple  ====')
print('===== Using tuple(), data type conversion [tuple + list] =====')

res = tuple( list(test_tup) + test_list)
print(res)