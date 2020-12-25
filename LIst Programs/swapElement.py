

print("========= size of list=========")
def swapList(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp
    return newlist

newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) 


print("\n========= swap in one line=========")
def swapList2(newlist2):
    newList2[0] , newList2[-1] = newList2[-1], newList2[0]
    return newList2

newList2 = [12, 35, 9, 56, 24] 
print(swapList(newList2))   


print("\n=========== usage of * operand==========")
def swapList3(newlist3):
    start, *middle, end = newlist3
    lst = [start, *middle, end]
    return lst

newList3 = [12, 35, 9, 56, 24] 
print(swapList(newList3))
