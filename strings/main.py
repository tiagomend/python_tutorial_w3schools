# Strings Multilinhas
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String são matrizes de bytes que representa caracteres Unicode
a = 'Hello, World!'
print(a[1])

# Loop em uma string
for x in 'banana':
    print(x)


# Comprimento da String
print(len(a))

# Verificar se determinados caracteres estão presentes
txt = 'The best things in life are free!'
if 'free' in txt:
    print('Yes, "free" is present.')

if 'expensive' not in txt:
    print('No, "expensive" is NOT present.')
