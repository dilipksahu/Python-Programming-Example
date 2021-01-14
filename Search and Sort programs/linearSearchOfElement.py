# Python Program for Linear Search

'''
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6
'''

def linearSearch(arr,x):
    print(arr)
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
lst = [ i for i in arr]
x = 110
print(linearSearch(lst,x))