# Print anagrams together in Python using List and Dictionary
# Anagram means all possible combination

# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'

def allAnagram(input):
    dic = {}
    for strval in input:
        key = ''.join(sorted(strval))
        # print(key)

        # check if key available in dic or else create 
        if key in dic.keys():
            dic[key].append(strval)
        else:
            dic[key] = []
            dic[key].append(strval)

    # dic = {'act': ['cat', 'tac', 'act'], 'dgo': ['dog', 'god']}
    # main type - 'act' and its type/anagram are 'cat', 'tac', 'act' 
    # print(dic)

    outcome = ''
    for key,value in dic.items():
        outcome = outcome + " ".join(value) + " "
    
    print(outcome)

arr = ['cat', 'dog', 'tac', 'god', 'act']
allAnagram(arr)