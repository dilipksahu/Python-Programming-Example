# program to check if a string is palindrome or not

print("======== String Slicing =========")
def isPalindrome1(s):
    rev = s[::-1]
    return rev

s = "malayalam"
ans = isPalindrome1(s)
if ans:
    print("Palindrme - Yes")
else:
    print("palindrome - No")


print("======= for loop =======")
def isPalindrome2(s):
    for i in range(0,int(len(s)/2)):
        # check char at index 0,1,2... with -1,-2,-3...
        if s[i] != s[len(s)-i-1]: 
            return False
    return True

# s = "malayalam"
s = "geeks"
if isPalindrome2(s):
    print("Palindrme - Yes")
else:
    print("palindrome - No")


print("====== Using one extra variable =======")
# s = "malayalam"
s = "geeks"
word = ""
for i in s:
    # reversing word
    word = i + word

if word == s:
    print("Palindrme - Yes")
else:
    print("palindrome - No")