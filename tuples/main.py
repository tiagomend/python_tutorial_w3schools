# Uma tupla é uma coleção ordenada e imutável
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

# Indexados
print(thistuple[0])
print(thistuple[1])
print(thistuple[2])

# Alterar valores de tupla (imutável)
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'Kiwi'
x = tuple(y)
print(x)

# Adicionar tupla a uma tupla
x = ('apple', 'banana', 'cherry')
y = ('orange',)
x += y
print(x)

# Para fazer alterações (adicionar, remover) em uma tupla, converta em list

# Descompactar uma tupla
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Usando Asterisco * caso o número de variáveis seja menor
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Fazer Loop em uma tupla é identico de como se faz em listas

# Juntar tuplas
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiplicar tuplas
fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2

print(mytuple)

# Métodos de Tupla
# Método count(value) - Número de vezes que um valor aparece na tupla
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# Método index(value) - Retorna a primeira ocorrencia de um valor
x = thistuple.index(8)
print(x)
