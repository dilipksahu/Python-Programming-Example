# Given an ordered dict, write a programm to insert items in beginning of ordered dict.

# Input: 
# original_dict = {'akshat':1, 'manjeet':2}
# item to be inserted ('nikhil', 3)

# Output:  {'nikhil':3, 'akshat':1, 'manjeet':2}

from collections import OrderedDict

ini_dict = OrderedDict({'akshat':1, 'manjeet':2})
ini_dict.update([('nikhil',3)])
# Adding beginning of ordered dict
ini_dict.move_to_end('nikhil', last= False)
print(ini_dict)