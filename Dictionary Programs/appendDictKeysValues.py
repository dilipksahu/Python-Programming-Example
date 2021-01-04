# Append Dictionary Keys and Values ( In order ) in dictionary

# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]
# Explanation : All the keys before all the values in list.

test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}

print("======= 1) Naive Method ======")
lst = []
for key in test_dict.keys():
    lst.append(key)

for value in test_dict.values():
    lst.append(value)

print(lst)


print('\n====== 2) concanating two list =====')
concat_list = list(test_dict.keys()) + list(test_dict.values())
print(concat_list)


print('\n===== 3) chain + keys + values ======')
from itertools import chain
chain_list = list(chain(test_dict.keys(), test_dict.values()))
print(chain_list)