# to add an item to end of the list use append() method
myList=["apple", "banana", "cherry"]
print(myList)
myList.append("orange")
print(myList)

# to add an item to specified index use insert method
myList.insert(1, "watermelon")
print(myList)

# to append elements from another list to our current list use extend() method
print(myList)
torpical=["mango", "pineapple", "papaya"]
myList.extend(torpical)
print(myList)

# add any other iterable object
print(myList)
tuple1=("kiwi", "orange")
myList.extend(tuple1)
print(myList)