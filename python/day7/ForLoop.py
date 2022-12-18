# print each item
fruits=["apple", "banana", "cherry", "kiwi"]

for x in fruits:
    print(x)

print("----------------------")

# loop each letter in string
for x in "AZAT":
    print(x)

print("----------------------")

# break keyword
for x in fruits:
    print(x)
    if x=="cherry":
        break

print("----------------------")

# continue
for x in fruits:
    if x=="cherry":
        continue
    print(x)

print("----------------------")

# using range() function
for x in range(6):
    print(x)

print("----------------------")
for x in range(2,6):
    print(x)

print("----------------------")
# we can increase the increment by adding parameter to range
for x in range(2, 30, 3):
    print(x)

print("----------------------")

# else block
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("----------------------")
# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("----------------------")
# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("----------------------")
# pass
for x in [0, 1, 2]:
  pass


