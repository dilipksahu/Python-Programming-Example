# Program to print duplicates from a list of integers

def duplicateElements(list1):
    final_list = []
    size = len(list1)
    for i in range(size):
        k = i + 1
        for j in range(k,size):
            if list1[i] == list1[j] and list1[i] not in final_list:
                final_list.append(list1[i])

    return final_list


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(*duplicateElements(list1))