# Python program to create a list of tuples from given list having number and its cube in each tuple

'''
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''

test_list = [9, 5, 6]

res_list = [ (n, pow(n,3)) for n in test_list]
print(res_list)