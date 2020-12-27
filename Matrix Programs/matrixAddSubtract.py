# Adding and Subtracting Matrices in Python

A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

print("======== Nested for loop ===================")
c = [[0,0],[0,0]]

for row in range(len(A)):
    for col in range(len(B[0])):
        c[row][col] = A[row][col] + B[row][col]

print(c)


print("======== List comp ==========")
add = [ [ A[row][col] + B[row][col] for col in range(len(A[0]))] for row in range(len(A))]
sub = [ [ A[row][col] - B[row][col] for col in range(len(A[0]))] for row in range(len(A))]
print(add)
print(sub)

print("======= Numpy =======")
import numpy as np
addition = np.add(A,B)
subtract = np.subtract(A,B)
print(addition,"\n",subtract)