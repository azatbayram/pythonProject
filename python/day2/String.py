# multi line string
x = """Hi, I am Azat.
I am 28 years old.
I am SDET"""

print(x)

# access values in String
a = "Hello, World!"
print(a[0])
print(a[3])
print(a[8])

print(a[0:4])
print(a[7:9])

# length of string
print(len(a))

# for loop string is array and we can loop through the characters
for x in "banana":
    print(x)

# checking string
txt="The best things in life are free!"
print("free" in txt)
print("azat"in txt)

# use checking tool in if statement
if "free" in txt:
    print("Yes,free is in txt")

