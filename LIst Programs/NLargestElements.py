# program to find N largest elements from a list

print("============Naive Method==========")
def Nmaxelements(list1,n):
    final_list = []
    for i in range(n):
        max1 = 0

        for j in range(0,len(list1)):
            if list1[j] > max1:
                max1 = list1[j]

        list1.remove(max1)
        final_list.append(max1)

    return final_list


list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
N = 3
print(*Nmaxelements(list1, N) )            # "*" removes square backets


print("============ Built-in method (sort)========")

l = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
n = 3
l.sort()
print(*l[-n:])
