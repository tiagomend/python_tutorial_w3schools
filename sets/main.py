# Conjunto [set] é uma coleção não ordenada e imutável

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# Não permite valores duplicados
# True e 1 são considerados duplicados
# False e 0 são considerados duplicados


# --------------------------------------------------------------------
thisset = {'apple', 'banana', 'cherry'}
print(len(thisset))

# Construtor set()
thisset = set(('apple', 'banana', 'cherry'))
print(type(thisset))

# --------------------------------------------------------------------
# Acessando itens de um set - percorrendo com um loop
for x in thisset:
    print(x)

# Verificar se um valor está presente em um conjunto
print('banana' in thisset)

# Adicionar itens ao um conjunto
thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')

print(thisset)

# Adicionar itens de outro conjunto ao conjunto atual
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

# Adicione qualquer iterável
thisset = {'apple', 'banana', 'cherry'}
mylist = ['kiwi', 'orange']

thisset.update(mylist)
print(thisset)

# Remover item
thisset.remove('banana')  # Se item não existir gera um erro
print(thisset)

thisset.discard('orange')  # Se item não existir não gera um erro
print(thisset)

# Remover item aleatório
thisset.pop()
print(thisset)

# Esvaziar um conjunto
thisset.clear()
print(thisset)

# Deletar um conjunto completamente
thisset = {'apple', 'banana', 'cherry'}
del thisset

try:
    print(thisset)
except:
    print('Conjunto não existe!')
