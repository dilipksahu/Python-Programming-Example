'''
Formula to calculate compound interest annually is given by:

A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span

'''


def compound_interest(p,r,t):
    a = p * (pow( (1 + r /100), t))
    CI = a - p
    return CI

p,r,t = list(map(float,input().split()))
print("Compound Interest = ",compound_interest(p,r,t))