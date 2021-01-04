# Python dictionary with keys having multiple inputs

# with multiple inputs in a key
print('==== Create dictionary with multiple inputs in a key =====')

dic = {}

# Insert first triplet in dictionary : {(10, 20, 30): 0}
x, y, z = 10, 20, 30
dic[x,y,z] = x + y - z

# Insert second triplet in dictionary : {(10, 20, 30): 0, (5, 2, 4): 3}
x, y, z = 5, 2 , 4
dic[x,y,z] = x + y - z

print(dic)

print('\n==== Access to the keys and values ======')
# dictionary containing longitude and latitude of places 
places = {("19.07'53.2", "72.54'51.0"):"Mumbai",
          ("28.33'34.1", "77.06'16.6"):"Delhi"} 

lat = []
log = []
plc = []
for i in places:
    lat.append(i[0])
    log.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(log)
print(plc)