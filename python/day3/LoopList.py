# print list items one by one using for loop
myList=["apple", "banana", "cherry", "orange"]
print("with for loop")
for x in myList:
    print(x)

# loop with range() and len() methods
print("with for loop by using range() and len() methods")
for x in range(len(myList)):
    print(myList[x])

# loop with while loop
print("with while loop")
i=0
while i<len(myList):
    print(myList[i])
    i+=1

# list comprehension loop
print("with list comprehension")
[print(x) for x in myList]



