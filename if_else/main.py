# Se
a = 33
b = 200
# A identação defini o escopo do código
if (b > a):
    print('b is greater than a')

# Se não Se
a = 33
b = 33
if (b > a):
    print('b is greater than a')
elif (a == b):
    print('a and b are equal')

# Se não
a = 200
b = 33
if (b > a):
    print('b is greater than a')
elif (a == b):
    print('a and b are equal')
else:
    print('a is greater than b')

# Se abreviado
if a > b: print('a is greater than b')


# Operador Ternário
a = 2
b = 330
print('A') if (a > b) else print('B')

# AND -> e
a = 200
b = 33
c = 500
if a > b and c > a:
    print('Both conditions are True')

# OR -> ou
a = 200
b = 33
c = 500
if a > b or c > a:
    print('At least one of the conditions is True')

# NOT -> não
a = 33
b = 200
if not a > b:
    print('a is NOT greater than b')

