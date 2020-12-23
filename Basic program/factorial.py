# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# =============== 1 =====================
print("Recursive and Ternary operator")

def factorial_R(n):
    return 1 if (n == 0 or n == 1)  else n * factorial_R(n - 1)

n = int(input("enter any non-negative number: "))
print(f"Factorial of {n} is",factorial_R(n))

# =============== 2 =======================
print("Iterative")

def factorial_I(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

n = int(input("enter any non-negative number: "))
print(f"Factorial of {n} is",factorial_I(n))


