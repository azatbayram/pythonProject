carInfo={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
carInfo.pop("model")
print(carInfo)
carInfo.update({"model":"Mustang"})

print("--------------------------")
print(carInfo)
carInfo.popitem()
print(carInfo)
carInfo.update({"model":"Mustang"})

print("--------------------------")
del carInfo["model"]
print(carInfo)
carInfo.update({"model":"Mustang"})

print("--------------------------")
carInfo.clear()
print(carInfo)