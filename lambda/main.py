# Uma função lambda é uma pequena função anônima
x = lambda a : a + 10
print(x(5))

# Podem receber qualquer número de argumentos
x = lambda a, b : a * b
print(x(5, 6))

# Função anônima dentro de outra função
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
print(mydoubler(10))
