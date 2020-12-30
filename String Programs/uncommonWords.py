# program to find uncommon words from two Strings

# Input : A = "apple banana mango" 
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

print("======== dictionary + list ========")
def uncommonWords(A, B):
    count = {}

    for word in A.split(" "):
        count[word] = count.get(word,0) + 1

    for word in B.split(" "):
        count[word] = count.get(word,0) + 1

    return [ word for word in count if count[word] == 1]

A = "apple banana mango" 
B = "banana fruits mango"
print(uncommonWords(A,B))


print("\n======= using empty string ======")
def uncommon(a, b):
    list_a = a.split()
    list_b = b.split()
    uc = ''
    for i in list_a:
        if i not in list_b:
            uc = uc+" "+i

    for i in list_b:
        if i not in list_a:
            uc = uc+" "+i

    return uc.split()

print(uncommon(A,B))



print("\n======== set.symmetric_difference =======")
def uncommonW(a, b):
    a = a.split()
    b = b.split()
    uncom =  set(a).symmetric_difference(set(b))
    return list(uncom)

print(uncommonW(A,B))