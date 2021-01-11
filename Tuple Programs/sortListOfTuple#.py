# Python program to sort a list of tuples by second Item

'''
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
'''
test_input = [('for', 24), ('is', 10), ('Geeks', 28),  
      ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)] 


print('======= Using the Bubble Sort ======')
# Bubble Sort is the simplest sorting algorithm that works by repeatedly 
# swapping the adjacent elements if they are in wrong order.
def Bubble_Sort(tup):
    length = len(tup)
    for i in range(0,length):
        for j in range(0, length-i-1):
            if tup[j][1] > tup[j + 1][1]:
                temp = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = temp
    return tup 

print(Bubble_Sort(test_input))


print('\n===== Using sort() =========')
def usingsort(tup):
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used 
    # tup.sort(key= lambda x: x[1])
    tup = sorted(tup, key=lambda x : x[1])
    return tup

print(usingsort(test_input))