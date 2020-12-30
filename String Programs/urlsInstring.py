#  Check for URL in a String

import re

def Find(string):
     regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
     url = re.findall(regex,string)
     return url

test_str =  'My Profile: \
            https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles \
            in the portal of http://www.geeksforgeeks.org/'
print("URLS: ",Find(test_str))