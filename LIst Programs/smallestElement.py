# program to find smallest number in a list

print("========= Naive Method ========")
l = [ i for i in input("List: ").split(" ")]

min1 = l[0]
for i in range(len(l)):
    if l[i] < min1:
        min1 = l[i]


print("Smallest Element: ",min1)

print("\n======= Ask for user input =========")

list1 = []

n =  int(input("Number of Element in List: "))
for i in range(n):
    ele = int(input("enter element: "))
    list1.append(ele)

print("Smallest element in List: ",min(list1))


# Note: Finding Largest can be used similar operation