file=open("demofile.txt", "rt")
print(file)

#print(file.read())

print("----------------------")

#print(file.read(5))

print("----------------------")

#print(file.readline())

for x in file:
    print(x)

file.close()
