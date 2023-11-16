# Herança em Python
class Person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person('John', 'Doe')
x.printname()

# Criando uma classe Filha
class Student(Person):
    pass

x = Student('Mike', 'Olsen')
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # Herda automaticamente
        self.graduationyear = year

    def welcome(self):
        print(f'Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}')

x = Student('Mike', 'Olsen', 2019)
x.printname()
x.welcome()
