# Dicionários são usados para armazenar valores de dados em pares chave:valor
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict['brand'])

# Comprimento do dict
print(len(thisdict))

# Construtor dict(**kwargs)
thisdict = dict(name='John', age=36, country='Norway')
print(thisdict)

# Acessando Itens do dicionário
# Pelo nome da chave
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict['model']
print(x)

# Pelo método get()
x = thisdict.get('brand')
print(x)

# --------------------------------------------------------------------
# Obter uma lista de todas as chaves
x = thisdict.keys()
print(x)
print(type(x))  # Retorna um objeto do tipo dict_keys

# Qualquer alteração no dicionário irá refletir no dict_keys objeto
print(x)

thisdict['color'] = 'white'
print(x)


# --------------------------------------------------------------------
# Obter uma lista de todos os valores
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

x = car.values()  # Retorna um objeto do tipo dict_values
print(x)

# Qualquer alteração no dicionário irá refletir no dict_values objeto
print(x)

car['color'] = 'white'
print(x)

# --------------------------------------------------------------------
# Obter uma lista de todos os itens
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

x = car.items()  # Retorna um objeto do tipo dict_items
print(x)

# Qualquer alteração no dicionário irá refletir no dict_items objeto
print(x)

car['color'] = 'white'
print(x)

# --------------------------------------------------------------------
# Verificar se uma chave existe
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

if 'model' in car:
    print('Yes, "model" is one of the keys in the thisdict dictionary')

# Mudar valores ou Adicionar valores
car['year'] = 2018
print(car)

# Atualizar dicionário (Mudar ou Adicionar)
car.update({'year': 2020})
print(car)

# --------------------------------------------------------------------
# REMOVENDO ITENS
# Método pop(value)
car.pop('model')
print(car)

# Método popitem() remove o último item inserido
car.popitem()
print(car)

# Método clear() - Esvazia o dicionário
car.clear()
print(car)

# --------------------------------------------------------------------
# ITERANDO EM UM DICIONÁRIO
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

# Imprimir os nomes de chaves
for x in car:
    print(x)

# Imprimir os valores do dicionário, um por um
for x in car:
    print(car[x])

# Usando o método values()
for x in car.values():
    print(x)

# Loop por chave e valores
for x, y in car.items():
    print(x, y)

# Copiar um dicionário
dict_copy = car.copy()
print(dict_copy)

# Outra maneira de fazer cópia
dict_copy = dict(car)
print(dict_copy)

# Criar dicionário com chaves e valores especificados com fromkeys()
x = ('a', 'b', 'c')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}


# Método setdefault()
x = car.setdefault('color', 'white')
print(x)
x = car.setdefault('model', 'Bronco')
print(x)
