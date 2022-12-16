x = "awesome" # global variable

def myfunc():
    #global x # refer to x global variable
    x = "fantastic" #local variable
    print("Python is "+x)
myfunc()

print("Python is "+x)