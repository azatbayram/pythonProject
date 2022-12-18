# add 10 to argument and return result
x=lambda a:a+10
print(x(5))

print("-----------------")

x=lambda a,b:a*b
print(x(3,6))

print("-----------------")

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("-----------------")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mytripler=myfunc(3)

print(mytripler(11))

print("-----------------")
