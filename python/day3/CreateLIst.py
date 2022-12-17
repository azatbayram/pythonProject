# There are two way of create list
# 1 normal way
list1=["apple", "banana", "cherry"]
print(list1)

# 2 with list constructor
list2=list(("apple", "cherry", "banana", "orange"))
print(list2)

# list is allows duplicates
list3=["apple", "banana", "apple", "cherry", "banana"]
print(list3)

# list length
print(len(list1))
print(len(list2))
print(len(list3))

# list can contains different data types
list4=["apple", 67, False, "cherry", 45.6]
print(list4)

# list is object
print(type(list4))
