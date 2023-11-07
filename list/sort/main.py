# Sort List - Ordenação
# Ordenar lista de forma Alfanumérica
thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort()
print(thislist)

# Ordenar numéricamente
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Ordem decrescente
thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Personalizar função de Ordenação


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Ordenação sem distinção entre maiúsculas e minúsculas
thislist = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist.sort()
print(thislist)

thislist = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist.sort(key=str.lower)
print(thislist)

# Inverter a ordem atual de uma lista
thislist = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist.reverse()
print(thislist)
