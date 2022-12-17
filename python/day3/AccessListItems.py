myList=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# access with index number. List index number is started with 0
print(myList[3])

# negative indexing
print(myList[-2])

# range of indexes starts with 2 but not including 5
print(myList[2:5])
print(myList[-4:-1])

# starts beginning
print(myList[:5])

# ends last item
print(myList[3:])

# if statement
if "apple" in myList:
    print("Yes, \'apple\' in the list")


