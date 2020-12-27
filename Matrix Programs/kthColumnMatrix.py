# Get Kth Column of Matrix

test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]] 

k = 2

print("======= List comp ========")
res = [ sub[k] for sub in test_list ]
print(res)


print("======= zip(*) ========")
rez =  list(zip(*test_list))[k]   
print(rez)