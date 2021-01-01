# String slicing in Python to rotate a string

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"

def string_slice(string, d):

    Lfirst = string[0:d]
    Lsecond = string[d:]
    Rfirst = string[0: len(string)-d]
    Rsecond = string[len(string)-d: ]

    # now concatenate two parts together 
    print("Left Rotation  : ",Lsecond + Lfirst)
    print("Right Rotation :", Rsecond + Rfirst)


s = "GeeksforGeeks"
d = 2
string_slice(s, d)