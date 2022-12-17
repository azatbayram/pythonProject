# first way of adding new item to dictionary
carInfo={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

print(carInfo)

carInfo["color"]="red"

print(carInfo)

carInfo.update({"year":2018})

print(carInfo)
