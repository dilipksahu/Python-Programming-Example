# Program for n-th Fibonacci number

print("=======Recursion======")
def fibonacci(n):
    if n <= 0:
        return 'Incorrect number'
    # First Fibonacci number is 0 
    elif n == 1:
        return 0
    # Second Fibonacci number is 1 
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input("Nth fibonacci numbers: "))))



print("=====Dynamic Recursion======")

fiboArr = [0,1]

def fibo(n):
    if n < 0:
        return "Incorrect Number"
    elif n <= len(fiboArr):
        return fiboArr[n - 1]
    else:
        temp = fibo(n - 1) + fibo(n - 2)
        fiboArr.append(temp)
        return temp

print(fibo(int(input("Nth fibonacci numbers: "))))
print(fiboArr)


print("==========Dynamic Programming with Space Optimization=======")


def fibooo(n):
    first , second = 0, 1
    if n < 0:
        return "Incorrect number"
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(2,n):
            fib = first + second
            first = second
            second = fib
        return second


print(fibooo(int(input("Nth fibonacci numbers: "))))