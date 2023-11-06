# Percorrendo uma Lista
# For Loop
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)

# Percorrer os números de índice
for i in range(len(thislist)):
    print(thislist[i])

# Usando um Loop While
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Loop usando List Comprehension
[print(x) for x in thislist]
