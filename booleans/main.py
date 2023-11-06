# Valores booleanos - True or False
print(10 > 9)  # Return True
print(10 == 9)  # Return False
print(10 < 9)  # Return False

# A instrução if returna um booleano (True ou False)
a = 200
b = 33

if b > a:
    print('b is greater than a')
else:
    print('b is not greater than a')

# Valores False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

# Definir um valor objeto como False


class MyClass():
    def __init__(self, x) -> None:
        self.x = x

    def __len__(self):  # Função dever retornar 0
        if self.x == 10:
            return 1
        else:
            return 0


myobj = MyClass(10)
print(bool(myobj))
myobj = MyClass(15)
print(bool(myobj))

# Funções podem retorna um booleano


def my_function():
    return True


print(my_function())

if my_function():
    print('YES!')
else:
    print('NO!')

# Verificar se um objeto é de um determinado tipo
x = 200
print(isinstance(x, int))
print(isinstance(x, float))
