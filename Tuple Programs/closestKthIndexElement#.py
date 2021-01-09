#  Closest Pair to Kth index element in Tuple

'''
Input :
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 2

Output : (19, 23)
'''

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
k = 1  # place index

print('====== 1. using enumerate() =======')
# any big number
min_dif = 99999999999999
# can take None or 0
res = None
for idx, val in enumerate(test_list):
    # least difference
    diff = abs(tup[k-1] - val[k - 1])
    if diff < min_dif:
        min_dif = diff
        res = idx

print("The nearest tuple to Kth index element is : " + str(test_list[res]))


print('====== 2. using min() + range() + lambda() =======')
index = min( range(len(test_list)), key = lambda idx : abs(test_list[idx][k-1] - tup[k-1]))
print("The nearest tuple to Kth index element is : " + str(test_list[index]))