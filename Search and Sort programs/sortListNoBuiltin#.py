# Python Program for Insertion Sort

# Insertion sort is a simple sorting algorithm that works 
# the way we sort playing cards in our hands.

def insertionSort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        j = i-1
        # if current value less than previous value then swap the values
        while j >=0 and curr < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        
        # if previous not greater current keep the current value
        arr[j+1] = curr
    return arr

arr = [12, 11, 13, 5, 6] 
print("Sorted List: ",insertionSort(arr))
