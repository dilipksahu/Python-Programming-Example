#  Check order of character in string using OrderedDict( )

# Input: 
# string = "engineers rock"
# pattern = "egr";
# Output: true
# Explanation: 
# one 'e' and 'g' in the input string are before all 'r'.

from collections import OrderedDict

def checkOrder(input, pattern):
    # output will be like  [('e', None), ('n', None), ('g', None), ('i', None),....]
    dic = OrderedDict.fromkeys(input)

    ptrnlen = 0
    for key,value in dic.items():
        # pattern string to check if order of characters  
        # are same or not 
        if key == pattern[ptrnlen]:
            ptrnlen = ptrnlen + 1

        # check if we have traverse complete  
        # pattern string 
        if ptrnlen == len(pattern):
            return 'true'

    # if we come out from for loop that means  
    # order was mismatched     
    return 'false'

input = 'engineers rock'
pattern = 'egr'
print(checkOrder(input, pattern))