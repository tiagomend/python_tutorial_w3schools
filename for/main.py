# O for loop é usado para iterar um sequência.
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# Loop em uma string
for x in 'banana':
    print(x)

# Instrução break para parar o loop
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# Instrução continue parar iteração atual e continuar com a próxima
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# Loop com um determinado número de vezes
for x in range(6):
    print(x)

# SE NÃO
for x in range(6):
    print(x)
else:
    print('Finally Finished!')

# Loops aninhados
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)
