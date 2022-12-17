# remove specified item
myList=["apple", "banana", "cherry", "orange", ]
print(myList)
myList.remove("banana")
print(myList)
#myList.remove("banana")
#print(myList)

myList.insert(1, "banana")

# pop() method remove specified index
print(myList)
myList.pop(1)
print(myList)
myList.insert(1, "banana")

# if we do not specify index pop() removes last one
myList.pop()
print(myList)

# del keyword also remove specified index
del myList[1]
print(myList)
myList.insert(1, "banana")

# we can also delete list with del keyword
# clear() method empties the list but not delete it
myList.clear()
print(myList)