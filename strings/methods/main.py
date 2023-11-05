# Método capitalize() - Primeiro caractere maiúsculo e o restante minúsculo
txt = 'python is FUN!'
print(txt.capitalize())

# Método casefold() - semelhante ao lower()
# Todos os caracteres minúsculos
txt =  'Hello, And Welcome To My World!'
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

# Método encode
txt = "My name is Ståle"
print(txt.encode())