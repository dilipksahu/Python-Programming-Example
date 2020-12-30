# Replace duplicate Occurrence in String

test_str = 'Gfg is best . Gfg also has Classes now. \
                Classes help understand better . ' 

print("======= for loop + enumerate =========")
# initializing replace mapping  
repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }

test_list = test_str.split()
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)

print(" ".join(test_list))


print("\n====== List Comp + enumerate ========")

test_list = test_str.split()
repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }
# below test_list.index['Gfg] = 0
test_list = [ repl_dict.get(ele) if ele in repl_dict and test_list.index(ele) != idx else ele for idx, ele in enumerate(test_list) ]

print(" ".join(test_list))