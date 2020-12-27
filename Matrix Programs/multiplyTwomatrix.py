# Python program to multiply two matrices

print("====== using nested for loop =======")
# take a 3x3 matrix 
A = [[12, 7, 3], 
    [4, 5, 6], 
    [7, 8, 9]]

# take a 3x4 matrix     
B = [[5, 8, 1, 2], 
    [6, 7, 3, 0], 
    [4, 5, 9, 1]] 

# empty  3X4 matrix
result = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 

# iterate through A rows 
for i in range(len(A)):
    # iterate through B columns
    for j in range(len(B[0])):
        # iterate through B rows
        for k in range(len(B)):   
            result[i][j] += A[i][k] * B[k][j]      # first iteration: 12*5 + 7*6 + 3*4 = 114

for i in result:
    print(i)


print("======== using list comp,zip and sum ===========")
lst = [ [ sum(a * b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
for i in lst:
    print(i)

print("======== using numpy =========")
import numpy as np
res = np.dot(A, B)
for i in res:
    print(i)