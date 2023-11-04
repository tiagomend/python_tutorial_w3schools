# Existem 3 tipos numéricos
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


# Inteiro positivo ou negativo
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Número de ponto flutuante positivo ou negativo
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Float com número científico "e" para indicar potência de 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)

# Números complexos escritos com 'j' como parte imaginária
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Conversão de tipo
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# De int para float
a = float(x)

# De float para int
b = int(y)

# De int para complex
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
# Não pode converte de complex para outro tipo numérico

# Número aleatório
import random

print(random.randrange(1, 10)) # entre 1 e 9
