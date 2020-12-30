# Find words which are greater than given length k

def geaterThanLength(string,k):
    s = string.split(" ")
    new_string = ""
    for i in s:
        if len(i) > k:
            new_string += i + " "

    print("Output: ",new_string)


test_str  = "hello geeks for geeks is computer science portal" 
k = 5
geaterThanLength(test_str,k)
