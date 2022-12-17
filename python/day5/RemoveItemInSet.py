# to remove item fromset use remove(), discard() or pop() method
mySet={"apple", "banana", "cherry"}
mySet.remove("banana")
print(mySet)
mySet.add("banana")

print("-----------------")
mySet.discard("cherry")
print(mySet)
mySet.add("cherry")

print("-----------------")
mySet.pop()
print(mySet)
mySet.add("apple")

print("-----------------")
mySet.clear()
print(mySet)

del mySet