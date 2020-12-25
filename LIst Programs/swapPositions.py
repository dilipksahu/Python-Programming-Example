

print("============ swap One liner============")
def swapPositions(newlist,pos1,pos2):
    newlist[pos1], newlist[pos2] = newlist[pos2] , newlist[pos1]
    return newlist

List = [23, 65, 19, 90] 
  
pos1, pos2  = 1, 3
print(swapPositions(List, pos1-1, pos2-1)) 


print("\n========== Tuple Variable=========")
def swapPos(newlist1,po1,po2):
    # Storing the two elements 
    # as a pair in a tuple variable get 
    get = newlist1[po1],newlist1[po2]         # get = (65, 90)
    # unpacking those elements 
    newlist1[po1] , newlist1[po2] = get
    return newlist1

List = [23, 65, 19, 90] 
po1, po2  = 1, 3
print(swapPos(List, po1, po2)) 
