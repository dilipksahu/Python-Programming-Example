# Generating random strings until a given string is generated

import random
import string
import time

# all possible characters including  
# lowercase, uppercase and special symbols 
# in any order
possibleCharacters = string.ascii_lowercase + string.digits + \
                     string.ascii_uppercase + ' ., !?;:'

# string to be generated 
t = "geek"
  
# To take input from user 
# t = input(str("Enter your target text: ")) 

attemptThis = ''.join(random.choice(possibleCharacters) 
                                for i in range(len(t)))

completed = False
iteration = 0

while completed == False:
    print(attemptThis)
    nextAttempt = ""
    completed = True

    # Fix the index if matches with  
    # the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            nextAttempt += random.choice(possibleCharacters)
        else:
            nextAttempt += t[i]

    iteration += 1
    attemptThis = nextAttempt
    time.sleep(0.1)

print("Target matched after " +
      str(iteration) + " iterations") 