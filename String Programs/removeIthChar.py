# Ways to remove i’th character from string in Python
# Removing char at pos 3 

print("======= using for loop =========")
test_str = "Geeksforgeeks"

new_str = ""
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("New String: ",new_str)
# This solution is much slower (has O(n^2) time complexity


print("======= Slice and concatination ========")
new_str1 = test_str[:2] + test_str[3:]
print("New String: ",new_str1)
# Similar in logic and is faster (it has O(n) time complexity).