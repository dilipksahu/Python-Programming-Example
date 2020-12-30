# Least Frequent Character in String

test_str = "GeeksforsGeeks"

print("======= Naive method + min ======")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res = min(all_freq, key= all_freq.get)
print("The least frequent character is ",res)



print("\n======= collections.Counter + min =========")
from collections import Counter

all_values = Counter(test_str)
# result = min(all_values, key= all_values.get)
result = min(all_values.keys(), key = lambda k: all_values[k])
print(all_values)
print("The least frequent character is ",result)
