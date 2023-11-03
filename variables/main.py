# Declarar variáveis
x = 5
y = 'John'
print(x)
print(y)

# Conversão para especificar o tipo
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# Obter o tipo com type()
print(type(x))
print(type(y))
print(type(z))

# Variáveis com múltiplas palavras
# Camel Case
myVariableName = 'myVariableName'
# Pascal Case
MyVariableName = 'MyVariableName'
# Snake Case
my_variable_name = 'my_variable_name'
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

# Multiplos valores para múltiplas variáveis
x, y, z = 'Orange', 'Banana', 'Cherry'
print(x)
print(y)
print(z)

# Um valor para múltiplas variáveis
x = y = z = 'Orange'
print(x)
print(y)
print(z)

# Descompactar uma coleção
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

# Variáveis de Saída
x = 'Python is awesome'
print(x)

x = 'Python'
y = 'is'
z = 'awesome'
print(x, y, z)  # Suporta tipos diferentes
print(x + " " + y + " " + z)  # Não suporte tipos diferentes
