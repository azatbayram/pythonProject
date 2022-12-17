# retrieve value
carInfo = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# first way
print(carInfo["year"])
# second way
print(carInfo.get("model"))

# get keys as list
x=carInfo.keys()
print(x)

#get values
y=carInfo.values()
print(y)

carInfo["color"]="white"
print(carInfo)

carInfo["year"]=2020
print(carInfo)

z=carInfo.items()
print(z)

if "model" in carInfo:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

