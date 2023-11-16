# Criar uma Classe
class MyClass:
    x = 5

# Instanciar um objeto
p1 = MyClass()
print(p1.x)

# Construtor em Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 36)

print(p1.name)
print(p1.age)

# Representação do objeto em String
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"

p1 = Person('John', 36)

print(p1)

# Métodos de objeto são funções exclusivas do objeto
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"

    def myfunc(self): # Self é uma referência a instância atual da classe
        print('Hello my name is ' + self.name)

p1 = Person('John', 36)
p1.myfunc()

# Modificar propriedades do objeto
p1.age = 40
print(p1.age)

# Excluir propriedades do objeto
del p1.age
try:
    print(p1.age)
except:
    print('Propriedade excluída')

# Excluir objeto
del p1
try:
    print(p1)
except:
    print('Objeto excluído')
