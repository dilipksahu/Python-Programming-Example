#  program to find second largest number in a list

# list of numbers - length of 
# list should be at least 2
list1 = [10, 20, 4, 45, 99,101]

mx = max(list1[0],list1[1])
secondmx = min(list1[0],list1[1])

for i in range(2,len(list1)):
    if list1[i] > mx:
        secondmx = mx
        mx = list1[i]
    elif list1[i] > secondmx and mx != list1[i]:
        secondmx = list1[i]

print("Second Largest Element = ",secondmx)