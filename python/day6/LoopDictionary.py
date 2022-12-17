carInfo={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":["white","red","black"]
}

for x in carInfo.keys():
    print(x)
print("-------------------")
for y in carInfo.values():
    print(y)
print("-------------------")
for x in carInfo:
    print(carInfo[x])
print("-------------------")

for x,y in carInfo.items():
    print(x,y)
    