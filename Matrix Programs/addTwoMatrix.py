# Python program to add two Matrices

print("========= using for loop ===========")
X = [[1,2,3], 
    [4 ,5,6], 
    [7 ,8,9]] 
  
Y = [[9,8,7], 
    [6,5,4], 
    [3,2,1]] 

Z = [[0,0,0],
    [0,0,0],
    [0,0,0]]

# iterate through rows 
for i in range(len(X)):         # rows = 3
    # iterate through columns
    for j in range(len(X[0])):      # columns = 3
        Z[i][j] =  X[i][j] + Y[i][j]

for i in Z:
    print(i)    


print("======== List Comp ============")
res = [ [ X[i][j] + Y[i][j] for j in range(len(X[0])) ] for i in range(len(X)) ]
for i in res:
    print(i)


print("=========== zip and sum ===========")
result = [ list(map(sum, zip(*t))) for t in zip(X, Y)] 
for i in result:
    print(i)