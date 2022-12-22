file=open("demofile2.txt", "w")
file.write("Now file has more content")
file.close()

file=open("demofile2.txt","r")
print(file.read())
file.close()

file=open("demofile2.txt", "w")
file.write("I added new line to file")
file.close()

file=open("demofile2.txt", "a")
file.write("\nOne more line")
file.close()

file=open("myfile.txt", "x")
file.close()