# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
# Input : [1, 2, 3, 4, 5, 6, 7] 
# Output : 3 4 5 6 7 1 2

print("==========Calling functions============")

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotateByOne(arr,n)

def leftRotateByOne(arr,n):
    temp = arr[0]
    for i in range(n-1):              # (n-1) array starts from  0 and last filled with temp
        arr[i] = arr[i+1]             # [2,3,4,5,6,7]
    arr[n-1] = temp                   # [3,4,5,6,7,1]

def printArray(arr,n):
    for i in range(n):
        print("%d"%arr[i],end=" ")


arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 


print("\n===============One Function=============")

def splitArray(arr,d,n):
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)   
splitArray(arr,2,n)

for i in range(n):
    print("%d"%arr[i],end=" ")