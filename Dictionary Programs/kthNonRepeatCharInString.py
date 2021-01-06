# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
'''
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.

'''
print('======= OrderedDict() + dict + list ========')
from collections import OrderedDict

def kthNonRepeat(input, k):
    # OrderedDict returns a dictionary data  
        # structure having characters of input  
    # string as keys in the same order they  
        # were inserted and 0 as their default value
    dic = OrderedDict.fromkeys(input, 0)
    
    for ch in input:
        dic[ch] += 1

    nonRepeatList = [ key for key,value in dic.items() if value == 1]

    if len(nonRepeatList) < k:
        return "Less than k non-repeating characters in input"
    else:
        return nonRepeatList[k-1]
        

string = "geeksforgeeks"
k = 3
print(kthNonRepeat(string, k))


print('\n====== get() + dict + list ======')

def kthRepeation(input, k):
    dic = {}

    for ch in input:
        dic[ch] = dic.get(ch,0) + 1

    lst = [ k for k,v in dic.items() if v == 1]

    if len(lst) < k:
        return "Less than k non-repeating characters in input"
    else:
        return lst[k-1]
    

print(kthRepeation(string, k))
