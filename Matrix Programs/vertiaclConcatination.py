#  Vertical Concatenation in Matrix

# Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]]
# Output : [‘Gfgis’, ‘goodfor’, “geeksbest”]

test_list = [["Gfg", "good"], ["is", "for"], ["Best"]] 


print("====== using while loop ========")
res = []
N = 0
while N != len(test_list):
    temp = ''
    for idx in test_list:
        try:
            temp = temp + idx[N]       # IndexError happens
        except IndexError:             
            pass
    res.append(temp)
    N = N + 1

res = [ ele for ele in res if ele]
print(res)


print("======== using For loop =======")
rez = []
for i in range(len(test_list)):
    temp = ''
    for idx in test_list:
        try:
            temp = temp + idx[i]
        except IndexError:
            pass

    rez.append(temp)

rez = [ ele for ele in rez if ele]
print(rez)


print("======= Using join() + list comprehension + zip_longest()  ========")
from itertools import zip_longest
result = ["".join(ele) for ele in list(zip_longest(*test_list, fillvalue=""))]
print(result)