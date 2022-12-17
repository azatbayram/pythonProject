# create new list that contains fruits item which one has a letter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList=[]

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# do the same job with list comprehension
newList.clear()

newList=[x for x in fruits if "a" in x]
print(newList)

# add items not apple
newList.clear()
newList=[x for x in fruits if x!="apple"]
print(newList)

# with no if statement
newList.clear()
newList=[x for x in fruits]
print(newList)

# create list 0 to 10 range
listNum=[x for x in range(10)]
print(listNum)

#create list 0 to 5
listNum.clear()
listNum=[x for x in range(10) if x<6]
print(listNum)

# create new list with upper case
newList.clear()
newList=[x.upper() for x in fruits]
print(newList)

# hello list
list2=["hello" for x in fruits]
print(list2)

# return orange insted of banana
newList.clear()
newList=[x if x!="banana" else "orange" for x in fruits]
print(newList)

