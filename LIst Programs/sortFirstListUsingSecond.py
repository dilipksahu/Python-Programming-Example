# Sort the values of first list using second list in Python

print("============= Using zip and sort function ==========")
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

def sort_list(list1,list2):
    zipped_pair = list(zip(y,x))
    z = [x for _,x in sorted(zipped_pair)]
    return z

print(sort_list(y,x))


print("================ Using dictionary,list comp and  lambda function =========")
def sort_the_elements(list1,list2):
    # Key and value pair from two list
    merge_dic = { list1[i] : list2[i] for i in range(len(list1))}   
    # sort dict based on values    
    merge_dic = { k:v for k,v in sorted(merge_dic.items(), key=lambda item: item[1] ) } 
    # Extract only keys      
    final_list = [ k for k in merge_dic.keys()]
    return final_list


print(sort_the_elements(x,y))
