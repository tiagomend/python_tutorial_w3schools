# Função é um bloco de código que só é executado quando é chamado.
def my_function():
    print('Hello from a function!')

# Chamando a função
my_function()

# Argumentos são informações passadas para a função
def my_function(fname):
    print(fname + ' Refsnes')

my_function('Emil')
my_function('Tobias')
my_function('Linus')

# Parâmetros -> variáveis listadas entre parêntese na definição da função
# Argumentos -> valores passados quando função é chamada

# Argumentos arbitrários *args
def my_function(*kids):
    print(kids) # Recebe uma tupla de argumentos
    print('The youngest child is ' + kids[2])

my_function('Emil', 'Tobias', 'Linus')

# Argumentos de palavras-chave arbitrárias, **kwargs
def my_function(**kid):
    print(kid) # Recebe um dicionário de argumentos
    print('His last name is ' + kid['lname'])

my_function(fname='Tobias', lname='Refsnes')

# Valor padrão para o parâmetro
def my_function(country='Norway'):
    print('I am from ' + country)

my_function('Sweden')
my_function('Brazil')
my_function()

# Valores de Retorno
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print(my_function(10))

# Recursão -> A função pode chamar a si mesma
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('\nRecursion Example')
tri_recursion(6)
