# update tuple
myTuple=("apple", "banana", "cherry")
y=list(myTuple)
y[1]="kiwi"
myTuple=tuple(y)

print(myTuple)

# add tuple
x=list(myTuple)
x.append("orange")
myTuple=tuple(x)

print(myTuple)

y=("banana",)
myTuple+=y

print(myTuple)

x=list(myTuple)
x.remove("kiwi")
myTuple=tuple(x)

print(myTuple)

# del keyword delete tuple completely
del myTuple
