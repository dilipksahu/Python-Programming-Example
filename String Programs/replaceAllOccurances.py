# Replace all occurrences of a substring in a string

# Input : test_str = “geeksforgeeks”
# s1 = “geeks”
# s2 = “abcd”
# Output : test_str = “abcdsforabcds”

test_str = "geeksforgeeks"

print("Original string:", test_str)
# convert to dictionary of each character
temp = str.maketrans('geek','abcd')
# Swap Binary substring 
test_str = test_str.translate(temp)
print("The string after swap : " + str(test_str))



