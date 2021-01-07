# Possible Words using given characters in Python

'''
Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal. 
'''

def possibleWords(Input, arr):
    for word in input:
        temp = ''
        for ch in word:
            if ch in arr:
                temp += ch
        if temp == word:
           print(word) 
    

input = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
possibleWords(input, arr)