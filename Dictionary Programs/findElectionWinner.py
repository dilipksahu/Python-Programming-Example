# Dictionary and counter in Python to find winner of election

print("======== Counter + Sorted + Slicing ========")
from collections import Counter

def winner(input):
    votes = Counter(input)

    dic = {}
    # output : {4: [], 2: [], 3: []}
    for value in votes.values():
        dic[value] = []

    # output : {4: ['john', 'johnny'], 2: ['jackie'], 3: ['jamie']}
    for key,value in votes.items():
        dic[value].append(key)

    # outout: [4, 3, 2] 
    # output : 4
    maxvote = sorted(dic.keys(), reverse=True)[0]

    # check if more than 1 candidates have same  
    # number of votes. If yes, then sort the list  
    # first and print first element  
    if len(dic[maxvote]) > 1:
        print(sorted(dic[maxvote])[0])
    else:
        print(dic[maxvote][0])


input = ['john','johnny','jackie','johnny', 
            'john','jackie','jamie','jamie', 
            'john','johnny','jamie','johnny', 
            'john']  
winner(input) 



print('\n====== shorter method using counter + max + list comp =======')
from collections import Counter

votes = ['john','johnny','jackie','johnny', 
            'john','jackie','jamie','jamie', 
            'john','johnny','jamie','johnny', 
            'john']

# output: Counter({'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2})
votes_count =  Counter(votes)

# output : 4
max_vote = max(votes_count.values())
# output : ['john', 'johnny']
lst = [ k for k,v in votes_count.items() if v == max_vote ]

# output: John
print(sorted(lst)[0])
