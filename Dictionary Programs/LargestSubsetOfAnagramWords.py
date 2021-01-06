# Python Counter to find the size of largest subset of anagram words

'''
Input: 
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3
'''
print('====== 1) Naive method =======')
def largestSubset(input):
    lst = input.split()
    dic = {}
    # sort each string in list
    for ch in lst:
        key = ''.join(sorted(ch))
        
        # check for avallable and if not create list then add
        if key in dic:
            dic[key].append(ch)
        else:
            dic[key] = []
            dic[key].append(ch)
    
    # Each key assign with number of items
    for key, val in dic.items():
        dic[key] = len(val)
        
    print(dic)
    # print max values
    maxlength = max(dic.values())
    print(maxlength)


string1 = "ant magenta magnate tan gnamate"
string2 = "cars bikes arcs steer"
largestSubset(string2)


print('\n====== 2) Counter() + list + max =====')
from collections import Counter
def maxAnagramSize(input):

    lst = input.split()

    # sort each string in lst and add to it
    for i in range(0,len(lst)):
        lst[i] = ''.join(sorted(lst[i]))

    dic = Counter(lst)

    print(max(dic.values()))

maxAnagramSize(string2)