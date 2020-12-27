# Transpose a matrix in Single line in Python
# converting matrix rows into columns


print('=========== List Comp =========')
m = [[1,2],[3,4],[5,6]]
print("Original Matrix \n",m)      # 3X2 matrix
rez = [[ m[row][col] for row in range(len(m))] for col in range(len(m[0])) ]
print("Transpose Matrix \n",rez)   # 2X3 matrix


print("=========== Numpy ==========")
import numpy as np
res = np.transpose(m)
print("Original Matrix \n",m)
print("Transpose Matrix \n",res)


print("======= numpy Array ========")
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix.T)