# Program to accept the strings which contains all vowels

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

print("===== set() + for loop ======")
def checkForVowels(string):
    # i.e vowels = {'a','e','i','o','u'}
    vowels = set("aeiou")
    s = set({})
    for ch in string.lower():
        if ch in vowels:
            s.add(ch)
        else:
            pass

    if len(s) == len(vowels):
        print("All vowels are present")
    else:
        print("All vowels are not present")

s = "ABeeIghiObhkUul"
# s = "geeksforgeeks"
checkForVowels(s)


print("====== set().intersection() method ========")
def check(string):
    if len(set(string.lower()).intersection("aeiou")) >= 5:
        print("All vowels are present")
    else:
        print("All vowels are not present")

check(s)