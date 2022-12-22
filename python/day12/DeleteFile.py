import os

#os.remove("myfile.txt")

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("The file is not exist")

os.rmdir("/Users/azatbayram/PycharmProjects/pythonProject/python/myfolder")
