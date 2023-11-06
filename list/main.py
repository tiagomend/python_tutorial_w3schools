# List
# - Armazenar vários itens em uma única variável
# - Lista é uma coleção ordenada, mutável, permite valores duplicados
thislist = ['apple', 'banana', 'cherry', 'apple']

print(thislist)
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[3])

# Comprimento da Lista
print(len(thislist))

# Pode conter tipos diferentes de dados
list_1 = ['abc', 34, True, 40.0, 'male']
print(list_1)

# Tipo
print(type(list_1))

# O Construtor list()
mytuple = ('apple', 'banana', 'cherry', 'apple')
thislist = list(mytuple)
print(mytuple)
print(thislist)

# Verificar se existe item
if 'apple' in thislist:
    print('Yes, "apple" is in the fruits list')

# --------------------------------------------------------------------
# Alterar valor do item
thislist = ['apple', 'banana', 'cherry', 'apple']
thislist[1] = 'blackcurrant'
print(thislist)

# Alterar um intervalo de valores de itens
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
thislist[1:3] = ['blackcurrent', 'watermelon']
print(thislist)

# Inserir mais itens do que substitui
thislist = ['apple', 'banana', 'cherry']
thislist[1:2] = ['blackcurrant', 'watermelon']
print(thislist)

# Inserir itens com insert()
thislist = ['apple', 'banana', 'cherry']
thislist.insert(2, 'watermelon')
print(thislist)

# --------------------------------------------------------------------
# Adicionar um item ao final da lista com append()
thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)

# Acrescentar elementos de outra lista à lista atual com extend()
thislist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
thislist.extend(tropical)
print(thislist)
# extend() aceita qualquer iterável

# --------------------------------------------------------------------
# Remover a primeira ocorrência de um item especificado
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# Remover índice especificado
thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)

# Remover o último item
thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# Esvaziar a lista
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)
