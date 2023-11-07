# Copiar uma lista
# list2 = list1 cria uma referência a list1 em list2
# Para cópia usar método copy() ou construtor list()

thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(id(thislist))
print(id(mylist))

mylist = list(thislist)
print(id(mylist))

mylist = thislist
print(id(mylist))
