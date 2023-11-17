# JSON é uma sintaxe para armazenar e trocar dados

# Importar o pacote integrado json
import json

# Analisar uma string JSON
x = '{"name":"John", "age":30, "city":"New York"}'

# Parse x -> converter para dicionário
y = json.loads(x)

print(y)
print(y['age'])
print(type(y))


# Converter de Python para JSON
x = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

y = json.dumps(x)

print(y)
print(type(y))
print(type(json.loads(y)))


# Formatar a String JSON
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x)) # Sem formatação
print(json.dumps(x, indent=4)) # Com recuo

# Ordenando o resultado
print(json.dumps(x, indent=4, sort_keys=True))
