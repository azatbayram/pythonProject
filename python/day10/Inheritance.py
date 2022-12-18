# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)


p1=Person("Azat", "Bayram")
p1.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear=year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


p2=Student("Agosh", "Gylyc", 2016)
p2.printname()

p3=Student("Azat","Bayram", 2016)
p3.welcome()
