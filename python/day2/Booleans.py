print(10<8)
print(10==8)
print(10>8)

a=37
b=45

if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))