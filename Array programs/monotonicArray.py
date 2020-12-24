# Program to check if given array is Monotonic
# An array is monotonic if it is either monotone increasing or monotone decreasing.

def isMonotonic(arr):

    return ( all(arr[i] <= arr[i+1]  for i in range(len(arr)-1)) or
             all(arr[i] >= arr[i+1]  for i in range(len(arr)-1))  )


A = [6, 5, 4, 4]
B = [10,15,20,12] 
print(isMonotonic(A))
print(isMonotonic(B))