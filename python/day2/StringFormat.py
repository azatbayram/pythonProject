# use format() method to combine str and number data types
age=27
txt="My name is Azat and I am {} yers old."
print(txt.format(age))

# multiple arguments with format() method
quantity=3
itemno=567
price=49.95
myOrder="I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity,itemno,price))

myOrder="I want {2} pieces of item {0} for {1} dollars."
print(myOrder.format(quantity,itemno,price))
