# Handling missing keys in Python dictionaries

country_code = {'India' : '0091', 
                'Australia' : '0025', 
                'Nepal' : '00977'}  

print('====== 1) get() method ======')
print(country_code.get('India', 'Not Found'))
print(country_code.get('Japan', 'Not Found'))


print('\n===== 2) setdefault() method =====')
# Set a default value for Japan 
country_code.setdefault('Japan', 'Not Present')
print(country_code['India'])
print(country_code['Japan'])


print('\n===== 3) collections.defaultdict() method ======')
from collections import defaultdict

# declaring defaultdict 
# sets default value 'Key Not found' to absent keys
def_dict = defaultdict( lambda : 'Key Not Found')

# initializing values 
def_dict['a'] = 1
def_dict['b'] = 3

# printing value
print(def_dict['a'])
print(def_dict['c'])