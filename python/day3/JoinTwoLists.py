# join two list with + operator
list1=["a", "b", "c"]
list2=[1, 2, 3]
list3=list1+list2
print(list3)

# join by using append and for loop

for x in list2:
    list1.append(x)

print(list1)
del list1[3:]

list1.extend(list2)
print(list1)
