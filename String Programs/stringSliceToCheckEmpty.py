# String slicing in Python to check if a string can become empty by recursive deletion

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.

def checkEmpty(string, sub_str):
    # If both are empty   
    if len(string) == 0 and len(sub_str) == 0:  
         return 'true'

    # If only pattern is empty  
    if len(string) == 0:  
         return 'true'

    while len(string) != 0:
        # find sub-string in main string 
        index = string.find(sub_str)

        # check if sub-string founded or not
        if index == -1:
            return 'false'

        # slice input string in two parts and concatenate
        string = string[0:index] + string[index + len(sub_str): ]

    # when string get empty return true
    return 'true'

string = "GEEGEEKSKS"
sub_str = "GEEKS"
print(checkEmpty(string, sub_str))