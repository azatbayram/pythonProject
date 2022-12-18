# simple compare operation with if statement

a=45
b=200

if b>a:
    print("b is greater than a")
elif a>b:
    print("a is greater than b")
else:
    print("a and b are epual")

# short hand if
if b>a: print("b is greater than a")

#short hand if else(ternory operators)
print("a") if a>b else print("b")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


a = 33
b = 200

if b > a:
  pass