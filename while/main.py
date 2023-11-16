# Executar um conjunto de instruções ENQUANTO uma condição for verdadeira
i = 1
while i < 6:
    print(i)
    i += 1

# Instrução que para o loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Parar a iteração atual e continuar com a próxima
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Executar um bloco de código quando a condição for falsa
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')
