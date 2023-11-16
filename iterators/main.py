# Iteradores Python - Objeto que contém um número contável de valores

# Iterador vs Iterável
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple) # Obtem um iterador

print(next(myit))
print(next(myit))
print(next(myit))

# Criar um iterador -> Deve implementar os métodos __iter__() e __next__()
class MyNumbers:
    # Iterador que retorne números começando com 1
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Parar Iteração
class MyNumbers:
    # Iterador que retorne números começando com 1
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
