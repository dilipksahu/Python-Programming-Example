# program to check whether the string is Symmetrical or Palindrome

'''
Given a string. the task is to check if the string is symmetrical 
and palindrome or not. A string is said to be symmetrical if both 
the halves of the string are the same and a string is said to be a 
palindrome string if one half of the string is the reverse of the 
other half or if a string appears same when read forward or backward.
'''

def isPalindrome(s):
    flag = 0
    for i in range(0,int(len(s)/2)):
        # check char at index 0,1,2... with -1,-2,-3...
        if s[i] != s[len(s)-i-1]: 
            flag = 1
            break
        else:
            flag = 0

    if flag == 0:
        print("The entered string is palindrome") 
    else:
        print("The entered string is not palindrome") 


def isSymmetrical(s):
    n = len(s)
    flag = 0
    if n%2:
        mid = n//2 + 1
    else:
        mid = n//2
    
    for i in range(0,n//2):
        if s[i] != s[mid+i]:
            flag = 1
        else:
            flag = 0
    
    if flag == 0:
        print("The entered string is symmetrical") 
    else:
        print("The entered string is not symmetrical") 

# s = "khokho"
s = "malayalam"
isPalindrome(s)
isSymmetrical(s)