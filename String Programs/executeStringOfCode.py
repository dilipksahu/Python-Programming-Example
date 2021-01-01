# Execute a String of Code in Python

'''
exec() function is used for the dynamic execution of Python code. 
It can take a block of code containing Python statements like loops,
class, function/method definitions and even try/except block. 
This function doesn’t return anything.
'''

def exec_code():
    code = '''
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

    return fact

print(factorial(8))
'''
    exec(code)

exec_code()