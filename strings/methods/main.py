# Método capitalize() - Primeiro caractere maiúsculo e o restante minúsculo
txt = 'python is FUN!'
print(txt.capitalize())

# Método casefold() - semelhante ao lower()
# Todos os caracteres minúsculos
txt = 'Hello, And Welcome To My World!'
print(txt.casefold())

# Método center() - 2 parametros (tamanho, caracter_de_preenchimento)
txt = 'banana'
print(txt.center(40, '-'))

# Método count() - Número de vezes que um valor aparece na string
# Parametros:
# value - valor
# start (opcional) - Posição inicial
# end (opcional) - Posição final
txt = 'I love apples, apple are my favorite fruit'
print(txt.count('apple'))
print(txt.count('apple', 10, 24))

# --------------------------------------------------------------------
# Método encode()
txt = "My name is Ståle"
print(txt.encode())
# Parametros:
# encoding - Define a codificação usada
# errors - Específica o metódo de erro

# Usa uma barra invertida no lugar do caractere não codificado
print(txt.encode(encoding='ascii', errors='backslashreplace'))

# Ignora os caracteres não codificados
print(txt.encode(encoding='ascii', errors='ignore'))

# Substitui o caractere por um texto explicando
print(txt.encode(encoding='ascii', errors='namereplace'))

# Gera um erro em caso de falha
# print(txt.encode(encoding='ascii', errors='strict'))

# Substitui o caractere por um ponto de interrogação
print(txt.encode(encoding='ascii', errors='replace'))

# Substitui o caractere por um caractere xml
print(txt.encode(encoding='ascii', errors='xmlcharrefreplace'))


# --------------------------------------------------------------------
# Método endswith(value, start, end)
# Retorna True se a string terminar com o valor específicado
txt = 'Hello, welcome to my world.'
print(txt.endswith('.'))
print(txt.endswith('my world.'))
print(txt.endswith('my world.', 5, 11))  # Parametros opcionais (start, end)

# --------------------------------------------------------------------
# Método expandtabs(tabsize) - especifica o espaço em branco do tab
txt = 'H\te\tl\tl\to'
print(txt.expandtabs())
print(txt.expandtabs(2))  # Parametro opcional (tabsize=8)

# --------------------------------------------------------------------
# Método find(value, start, end)
# Encontra a primeira ocorrência do valor específicado
# Retorna -1 se o valor não for encontrado [index() gera exceção]
txt = 'Hello, welcome to my world.'
print(txt.find('welcome'))

# --------------------------------------------------------------------
# Método isalnum()
# Retorna True se todos os caracteres forem alfanuméricos
txt = 'Company12'
print(txt.isalnum())
txt = 'Company 12'
print(txt.isalnum())  # Return False

# --------------------------------------------------------------------
# Método isalpha()
# Verifica se todos os caracteres são letras do alfabeto (a-z)
txt = 'CompanyX'
print(txt.isalpha())

# --------------------------------------------------------------------
# Método isascii()
# Verifica se todos os caracteres são ASCII
txt = 'Company123'
print(txt.isascii())

# Método isdecimal()
# Verifica se todos os caracteres são decimais (0-9)
txt = '1234'
print(txt.isdecimal())

# Método isdigit()
# Retorna True se todos os caracteres forem dígitos
txt = '50800'
print(txt.isdigit())

# Método isidentifier()
# Verifica se a string é um identificador válido
txt = 'first_name'
print(txt.isidentifier())

# Método islower()
# Verifica se todos os caracteres estão em letras minúsculas
txt = 'hello world!'
print(txt.islower())

# Método isprintable()
txt = 'Hello!\nAre You #1?'
print(txt.isprintable())  # Return False

# Método isspace()
# Verifica se todos os caracteres são espaços em branco
txt = '   '
print(txt.isspace())  # Return True

# Método istitle()
txt = 'Hello, And Welcome To My World!'
print(txt.istitle())  # Return True
txt = 'HELLO, AND WELCOME TO MY WORLD!'
print(txt.istitle())  # Return False

# Método isupper()
print(txt.isupper())  # Return True

# --------------------------------------------------------------------
# Método join(iterable)
# Pega todos os itens de um iterável e os une em uma string
my_iterable = ('John', 'Peter', 'Vicky')
separator = ' '
print(separator.join(my_iterable))

# --------------------------------------------------------------------
# Método ljust(length, character)
# Alinha à esquerda usando o caractere especificado [space]
txt = 'banana'
x = txt.ljust(20)
print(x, 'is my favorite fruit.')
x = txt.ljust(20, '_')
print(x, 'is my favorite fruit.')

# --------------------------------------------------------------------
# Método lstrip(characters)
# Remove caracteres iniciais à esquerda [espaço é o caractere padrão]
txt = '   banana   '
print(txt.lstrip())
txt = '_____banana_'
print(txt.lstrip('_'))
# strip() remove dos dois lados
print(txt.strip('_'))

# --------------------------------------------------------------------
# Método partition(value)
# Divide a string em uma tupla contendo três elementos
txt = 'I could eat bananas all day'
print(txt.partition('bananas'))

# Método replace(oldvalue, newvalue, count)
# Substitui um valor especificado por outro valor especificado
txt = 'I like bananas'
print(txt.replace('bananas', 'apples'))
txt = "one one was a race horse, two two was one too."
# Substitui as duas primeiras ocorrências
print(txt.replace('one', 'three', 2))

# --------------------------------------------------------------------
# Método rfinc(value, start, end)
# Encontra a última ocorrência do valor
txt = 'Mi casa, su casa.'
print(txt.rfind('casa'))  # Semelhante ao rindex()

# Método rjust(length, character)
txt = 'banana'
x = txt.rjust(20)
print(x, 'is my favorite fruit')
x = txt.rjust(20, '_')
print(x, 'is my favorite fruit')

# --------------------------------------------------------------------
# Método split(separator, maxsplit)
txt = 'Welcome to the jungle'
print(txt.split())
print(txt.split(maxsplit=1))  # Lista com 2 itens

# --------------------------------------------------------------------
# Método splitlines(keepends)
txt = '''Thank you for the music
Welcome to the jungle'''
print(txt.splitlines())
print(txt.splitlines(keepends=True))

# --------------------------------------------------------------------
# Método startswith(value, start, end)
txt = 'Hello, welcome to my world.'
print(txt.startswith('Hello'))

# --------------------------------------------------------------------
# Método swapcase()
# Colcca minúsculas em maiúsculas e vice-versa
txt = 'Hello My Name Is PETER'
print(txt.swapcase())

# Método zfill(len)
# Adiciona zeros (0) no início da string até atingir o comprimento
txt = 'hello'
print(txt.zfill(10))
