# Remove all duplicates from a given string in Python

# Input : geeksforgeeks
# Output : Without Order =  egfkosr
#          With Order    =  geksfor

print("====== Naive method =======")
def removeDup(string):
    s = set(string)
    s = "".join(s)
    print("Without Order = ",s)
    t = ""
    for i in string:
        if i in t:
            pass
        else:
            t = t + i
    print("With Order    = ",t)


s ="geeksforgeeks"
removeDup(s)


print("\n===== using collections.orderedDict + fromkeys ========")
def removeDupWithoutOrder(string):
    s = "".join(set(string))
    print("Without Order = ",s)

from collections import OrderedDict
def removeDupWithOrder(string):
    s = OrderedDict.fromkeys(string)
    print("with Order = ","".join(s))

removeDupWithoutOrder(s)
removeDupWithOrder(s)