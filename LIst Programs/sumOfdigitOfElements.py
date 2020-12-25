#  Sum of number digits in List

print("========= Naive method =========")
def sumOfdigits(list1):
    final_list = []

    for ele in list1:
        sum1 = 0
        for i in str(ele):
            sum1 += int(i)
        final_list.append(sum1)

    return final_list

list1 = [12, 67, 98, 34]
print(sumOfdigits(list1))


print("========== list comp and map ===========")
def sumOfdig(l):
    lst = list(map( lambda ele : sum( int(x) for x in str(ele) ), l))
    return lst

l = [12, 67, 98, 34] 
print(sumOfdig(l))

