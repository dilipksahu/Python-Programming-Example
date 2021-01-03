# Convert key-values list to flat dictionary

# The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]}
# Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

'''
Method : zip() + dict()
The combination of above functions can be used to achieve the required task.
In this, we perform the pairing using zip() and dict() is used to convert 
tuple data returned by zip() to dictionary format.

'''
test_dict = {'month' : [1, 2, 3], 
             'name' : ['Jan', 'Feb', 'March']}

print("===== zip() + dict() ========")
print(dict(zip(test_dict['month'], test_dict['name'])))

