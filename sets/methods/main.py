# Método copy() - Retorna uma cópia do set
fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
print(x)
print(id(fruits))
print(id(x))

# Método difference(set) - Retorna um conjunto com a diferença entre dois conjuntos
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)
z = y.difference(x)
print(z)

# Método difference_update(*set)
# Em vez de retornar um conjunto novo altera o conjunto original
x.difference_update(y)
print(x)

# Método intersection(set) - Retorna um conjunto com itens que existem em x e y
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.intersection(y)  # Pode receber mais de um conjunto
print(z)

# Método intersection_update(*set)
# Em vez de retornar um conjunto novo altera o conjunto original
x.intersection_update(y)
print(x)

# Método isdisjoint(set) - True se for disjuntos
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'facebook'}

z = x.isdisjoint(y)
print(z)

# Método issubset(set) - True se for subconjunto
x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}

z = x.issubset(y)
print(z)

# Método issuperset(set) - True se for superconjunto
z = y.issuperset(x)
print(z)

# Método symmetric_difference(set)
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.symmetric_difference(y)
print(z)

x.symmetric_difference_update(y)
print(x)

# Método union(*set) - Retorna um conjunto com a união de todos os conjuntos
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.union(y)
print(z)
