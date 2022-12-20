myTuple=("apple", "banana", "cherry", "kiwi")
myIterator=iter(myTuple)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

name="Azat"
myIt=iter(name)

print(next(myIt))
print(next(myIt))

for x in myTuple:
    print(x)

for x in name:
    print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))