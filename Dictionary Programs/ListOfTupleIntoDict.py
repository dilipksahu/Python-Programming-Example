# Convert a list of Tuples into Dictionary

'''
Input : [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output : {'akash': [10], 'gaurav': [12], 'anand': [14], 
          'ashish': [30], 'akhil': [25], 'suraj': [20]}
'''
print('====== 1) Naive Method ======')
def convert(input, dic):
    for tup in input:
        if tup[0] in dic:
            dic[tup[0]].append(tup[1])
        else:
            dic[tup[0]] = []
            dic[tup[0]].append(tup[1])
    print(dic)

input = [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dic = {}
convert(input,dic)


print('\n===== 2) setdefault() =======')
def setDefault(input, dic):
    for a, b in input:
        dic.setdefault(a, []).append(b)

    print(dic)

setDefault(input,dic)


print('\n======= 3) dict() =======')
# it gives dictionary but not list values
print(dict(input))