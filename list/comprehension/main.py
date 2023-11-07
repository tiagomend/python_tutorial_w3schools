# List Comprehension - Sintaxe curta para criar nova lista com base em outra
# Sem List Comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# Com List Comprehension
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# Condição pode ser omitida
newlist = [x for x in fruits]
print(newlist)

# Pode ser usado qualquer objeto iterável
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# A expresão pode ser manipulada antes que acabe como item da lista
newlist = [x + x for x in range(10)]
print(newlist)

# A expressão pode conter condições para manipular o resultado
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)
