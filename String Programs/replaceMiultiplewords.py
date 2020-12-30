# Replace multiple words with K

test_str = 'Geeksforgeeks is best for geeks and CS'

print("======== for loop + join ======")
test_str = test_str.split()
repl_word = ['best','for','CS']
k = 'gfg'

for i in range(len(test_str)):
    if test_str[i] in repl_word:
        test_str[i] = k

print(" ".join(test_str))

print("\n====== List comp + join ========")
test_string = 'Geeksforgeeks is best for geeks and CS'
repl_word = ['best','for','CS']
k = 'gfg'
res = [ k if i in repl_word else i for i in test_string.split()]
print(" ".join(res))



