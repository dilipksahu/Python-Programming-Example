# Find the size of a Tuple in Python

# The size of a Tuple means the amount of memory (in bytes) taken by a Tuple object. 
# In this article, we will learn various ways to get the size of a python Tuple.

print('======== 1.Using getsizeof() function =======')
import sys

# sample Tuples 
Tuple1 = ("A", 1, "B", 2, "C", 3) 
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu") 
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")) 

print('Size of tuple1 is ' + str(sys.getsizeof(Tuple1))+ ' bytes' )
print('Size of tuple2 is ' + str(sys.getsizeof(Tuple2))+ ' bytes' )
print('Size of tuple3 is ' + str(sys.getsizeof(Tuple3))+ ' bytes' )


# Note:The sys.getsizeof() function includes the marginal space usage, 
# which includes the garbage collection overhead for the object. 
# Meaning it returns the total space occupied by the object in addition 
# to the garbage collection overhead for the spaces being used.

print('========= Using inbuilt __sizeof__() method ========')

# Python also has an inbuilt __sizeof__() method to determine the space 
# allocation of an object without any additional garbage value.

print('Size of tuple1 is ' + str(Tuple1.__sizeof__()) + ' bytes')
print('Size of tuple2 is ' + str(Tuple2.__sizeof__()) + ' bytes')
print('Size of tuple3 is ' + str(Tuple3.__sizeof__()) + ' bytes')