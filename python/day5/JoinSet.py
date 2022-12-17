# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c", 2}
set2 = {1, 2, 3, "a"}

set3=set1.union(set2)
print(set3)

print("----------------")
set1.update(set2)
print(set1)

print("----------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)


print("----------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)


print("----------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

print("----------------")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)