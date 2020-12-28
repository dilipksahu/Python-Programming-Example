# Check if a Substring is Present in a Given String

print("====== Using find() method ========")
def checkByFind(string,substring):
    # find() function returns -1 if it is not found, else it returns the first occurrence.
    if string.find(substring) == -1:
        print("NO")
    else:
        print("YES")

string = "geeks for geeks"
sub_str ="geek"
checkByFind(string,sub_str)


print("========= using count() method =======")
def checkByCount(str1,str2):
    if str1.count(str2) > 0:
        print("YES")
    else:
        print("NO")

checkByCount(string,sub_str)


print("======= using Regex search() method ======")
import re

if re.search(sub_str,string):
    print("Yes")
else:
    print("No")