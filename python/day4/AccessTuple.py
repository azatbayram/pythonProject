# access tuple items with index
myTuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myTuple[2])

# access with negative index
print(myTuple[-3])

# range of index
print(myTuple[2:5])
print(myTuple[:6])
print(myTuple[2:])
print(myTuple[-4:-2])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")