# Break a list into chunks of size N in Python


print("========= Naive method ========")
def divide_chunck(l, n):
    for i in range(0,len(l),n):   # starts with 'geeks','nerdy','life'
        yield l[ i : i + n ]



my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 
n = 5
output = list(divide_chunck(my_list,n))
print(output)


print("======== List Comp ==========")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

n = 4

x = [ l[ i : i+n ] for i in range(0,len(l),n)]
print(x)