
# Program to find a number is prime or not

n = int(input("Enter any number: "))

if n < 1:
    print("Not valid number...")
else:
    for i in range(2,n//2):
        if n % i == 0:
            print(f'{n} is Not a prime number')
            break
    else:
        print(f'{n} is prime number')

        
        