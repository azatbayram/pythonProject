# add item to set
mySet={"apple", "banana", "cherry"}
mySet.add("orange")
print(mySet)

print("----------------")

tropical={"pineapple", "mango", "papaya"}
mySet.update(tropical)
print(mySet)

print("-----------")

myList=["kiwi", "blackcurrant"]
mySet.update(myList)
print(mySet)