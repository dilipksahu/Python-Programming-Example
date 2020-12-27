#  Matrix creation of n*n

N  = 4

print("========== List comp ==========")
matrix = [ list(range(1 + N * i, 1 + N * (i + 1))) for i in range(N)]
print(matrix)



print("======== using next() + itertools.count() ========")
from itertools import count

temp = count(1)     #  start from 1 number      
# matrix creation of n * n    
res = [ [ next(temp) for i in range(N)] for i in range(N)]
print(res)