# Count the Number of matching characters in a pair of string

# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5 
# (i.e. matching characters :- b, 1, 2, @, k)

print("======== use string.find(character) ========")
# This returns the first occurrence index of character in string, if found, otherwise return -1.

def count(str1,str2):
    c = j = 0
    for i in str1:
        # this will check if character extracted from 
        # str1 is present in str2 or not(str2.find(i) 
        # return -1 if not found otherwise return the  
        # starting occurrence index of that character 
        # in str2) and j == str1.find(i) is used to  
        # avoid the counting of the duplicate characters 
        # present in str1 found in str2 
        if str2.find(i) >= 0 and j == str1.find(i):
            c = c + 1
        j = j + 1
    print('No. of matching characters are : ', c)


str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
count(str1,str2)


print("\n======= set + set(intersection) =========")

def counting(str1,str2):
    set_string1 = set(str1)
    set_string2 = set(str2)
    # using (&) intersection mathematical operation on sets 
    # the unique characters present in both the strings 
    # are stored in matched_characters set variable 
    # match_char = set_string1.intersection(set_string2)
    match_char = set_string1 & set_string2
    print('No. of matching characters are : ', len(match_char)) 

counting(str1,str2)


print("\n====== re.search() ========")
import re
count = 0
for i in str1:
    if re.search(i,str2):        #  it counts duplicate values 
        count += 1

print('No. of matching characters are : ',count)    