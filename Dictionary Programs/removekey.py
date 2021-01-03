# Ways to remove a key from dictionary

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21} 

def removeBydel(dic):
    print('======== using del =========')
    print("Before remove: " + str(dic))

    del dic["Mani"]

    print("After removed:" + str(dic))

removeBydel(test_dict)


print('======= using pop =========')

def removeBypop(dic):
    print("Before remove :" + str(dic))
    remvomed_value = dic.pop('Haritha')
    print("After removed: " + str(dic))
    print("Removed dict key value: " + str(remvomed_value))

    # If key not available than pop can return default value
    remvomed_value = dic.pop('Haritha', 'No key found')
    print("After removed: " + str(dic))
    print("Removed dict key value: " + str(remvomed_value))

removeBypop(test_dict)


print("\n===== using item() + dict comp =======")

def returnDict(dic):
    print("Original Dict: "+ str(test_dict))
    res = { k:v for k,v in dic.items() if k != 'Mani' }
    print("After removed:" + str(res))

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21} 
returnDict(test_dict)