# Program to check if a string contains any special character

# Input : Geeks$For$Geeks
# Output : String is not accepted.

import re

def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if re.search(regex, string) == None:
        print("String is accepted")
    else:
        print("String is not accepted")

s = "GeeksForGeeks"
run(s)