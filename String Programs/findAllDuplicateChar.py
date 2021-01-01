# Find all duplicate characters in string

# Input : geeksforgeeeks
# Output : e g k s

print("======== for loop, dict and list =====")
def checkDuplicateChar(string):
    all_char = {}
    for ch in string:
        all_char[ch] = all_char.get(ch,0) + 1
    
    dup_char = [ k for k in all_char if all_char[k] > 1]
    print(" ".join(sorted(dup_char)))

Input = "geeksforgeeeks"
checkDuplicateChar(Input)


print("\n====== collections.Counter() =======")
from collections import Counter

def findDupChar(string):
    all_char = Counter(string)
    dup_char = [ k  for k,v in all_char.items() if v > 1]
    print(" ".join(sorted(dup_char)))

findDupChar(Input)