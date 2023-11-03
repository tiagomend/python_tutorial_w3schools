# Variáveis global
x = 'awesome'


def myfunc():
    global y
    y = 'fantastic'
    x = y
    print('Python is ' + x)


myfunc()

print('Python is ' + y)

# Alterando variavel global dentro de uma função
z = 'awesome'


def myfunc2():
    global z
    z = 'fantastic'


myfunc2()
print('Python is ' + z)
