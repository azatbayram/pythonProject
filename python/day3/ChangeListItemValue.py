# change list item value with index
list1=["apple", "banana", "cherry"]
print(list1)
list1[1]="blackcurrant"
print(list1)

# change a range of item value
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(list2)
list2[1:3]=["blackcurrant", "watermelon"]
print(list2)

list3 = ["apple", "banana", "cherry"]
list3[1:2] = ["blackcurrant", "watermelon"]
print(list3)

list4 = ["apple", "banana", "cherry"]
list4[1:3] = ["watermelon"]
print(list4)

# insert new item to the list
list5=["apple", "banana", "cherry"]
list5.insert(2, "watermelon")
print(list5)
