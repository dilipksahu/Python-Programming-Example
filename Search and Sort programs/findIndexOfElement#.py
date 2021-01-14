# Python Program for Binary Search (Recursive and Iterative)

arr = [ 2, 3, 4, 10, 40 ] 
x = 10

print('====== 1.) Recursive =======')
def recursive_search(arr,low,high,x):
    mid = (high + low)//2
    if high >= low:
        # If element is present at the middle itself 
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only 
        # be present in left subarray
        elif arr[mid] > x:
            return recursive_search(arr,low,mid-1,x)
        # Else the element can only be present in right subarray
        else:
            return recursive_search(arr,mid+1,high,x)
    else:
        return -1


result = recursive_search(arr,0,len(arr)-1,x)
if result != -1:
    print("Element present at index " + str(result))
else:
    print("Element not present in array")


print('\n======= 2.) While loop ========')
def Iterative1(arr,x):
    low = 0
    high = len(arr)-1
    
    while high >= low:
        mid = high + low // 2
        # check element present in left
        if arr[mid] > x:
            high = mid - 1
        # check element present in right
        elif arr[mid] < x:
            low = mid + 1
        # element equal to mid value
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

result = Iterative1(arr,x)
if result != -1:
    print("Element present at index " + str(result))
else:
    print("Element not present in array")



print('\n===== 3.) For Loop ========')
def iterative2(arr,x):
    high = len(arr) - 1
    low = 0
    mid = high + low //2
    if x in arr:
        if arr[mid] > x:
            # check for element present in left side
            for i in range(low,mid):
                if arr[i] == x:
                    return i
        elif arr[mid] < x:
            for i in range(mid+1,high):
                if arr[mid] == x:
                    return i
        else:
            return mid
    else:
        return -1

result = iterative2(arr,x)
if result != -1:
    print("Element present at index " + str(result))
else:
    print("Element not present in array")



# Note: Recomended method is While loop and recursive 