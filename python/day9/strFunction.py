class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name},{self.age}"

    def myFunc(self):
        print("Hello my name is " + self.name)

p1=Person("Azat", 27)

print(p1)

p1.myFunc()


