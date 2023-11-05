# String em Maiúscula
a = 'Hello, World!'
print(a.upper())

# String em Minúsculo
print(a.lower())

# Remover espaços em branco do início ou do fim
a = ' Hello, World! '
print(a.strip())

# Substituir uma String por outra String
a = 'Hello, World!'
print(a.replace('H', 'J'))

# Dividir uma String em substrings dentro de uma lista
print(a.split(','))

# Formatação de String
qty = 3
item_code = 567
price = 49.95
order = 'I want to pay {2} dollars for {0} pieces of item {1}.'

print(order.format(qty, item_code, price))
