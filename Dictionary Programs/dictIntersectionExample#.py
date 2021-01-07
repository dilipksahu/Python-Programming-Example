# Python counter and dictionary intersection example 
# (Make a string using deletion and rearrangement)

'''
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible
'''
from collections import Counter

def dictIntersection(str1,str2):
    # convert both strings into dictionaries 
    # output will be like 
    # str1="aabbcc", dict1={'a':2,'b':2,'c':2} 
    # str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}
    dic1 = Counter(str1)
    dic2 = Counter(str2)

    # take intersection of two dictionries 
    # output will be result = {'a':1,'b':2,'c':2}
    result = dic1 & dic2
    
    # compare resultant dictionary with first 
    # dictionary comparison first compares keys 
    # and then compares their corresponding values
    return result == dic1

# s1 = 'ABHISHEKsinGH'
# s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
s1 = 'Hello'
s2 = 'dnaKfhelddf'
if dictIntersection(s1, s2):
    print("Possible")
else:
    print("Not possible")