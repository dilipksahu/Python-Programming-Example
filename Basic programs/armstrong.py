'''
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1253
Output : No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

'''
# function to check digit length
def order(x): 
  
    # Variable to store of the number 
    n = 0
    while (x != 0): 
        n = n + 1
        x = x // 10
          
    return n

def armstrong(x):    
    rem = 0
    arm = 0
    n = order(x)

    temp = x
    while temp != 0:	
        rem=temp%10
        arm = arm + (rem**n)
        temp = temp//10
    if arm == num:
        print('Yes')
    else:
        print('No')

num=int(input('Enter the number=>'))
armstrong(num)
