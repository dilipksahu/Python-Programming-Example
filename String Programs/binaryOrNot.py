# Check if a given string is binary string or not

print("======= useing set() =========")
def check(string):
    s = set(string)
    p = {'0','1'}
    if s == p or s == {'0'} or s == {'1'}:
        print("Yes")
    else:
        print("No")

test_string1 = "101010000111"
test_string2 = "geeks101"
check(test_string1)
check(test_string2)


print("\n====== for loop ========")
def run(string):
    p = "10"
    flag = 0
    for i in string:
        if i not in p:
            flag = 1
            break
        else:
            pass

    if flag:
        print("No")
    else:
        print("Yes")

run(test_string1)
run(test_string2)

