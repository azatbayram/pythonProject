import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y=json.loads(x)

print(y)

print(y["age"])

z = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(z, indent=4))

print(json.dumps(z, indent=4, sort_keys=True))

print(json.dumps(z, indent=4,separators=(".", "=")))