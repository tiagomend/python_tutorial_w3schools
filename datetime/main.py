# Data em Python com o módulo datetime
import datetime

x = datetime.datetime.now() # Data atual
print(x)

# Retornar o Ano
print(x.year)

# Retornar o nome do dia da semana
print(x.strftime('%A'))

# Criando um objeto de data
x = datetime.datetime(2020, 5, 17)
print(x)

# Método para formatar data em Strings Legíveis
x = datetime.datetime(2018, 12, 1)
print(x.strftime('%B'))

print(x.strftime('%a')) # exemplo 'Wed'
print(x.strftime('%A')) # exemplo 'Wednesday'
print(x.strftime('%w')) # exemplo '3' -> semana entre 0-6
print(x.strftime('%d')) # exemplo '31' -> dia entre 1-31
print(x.strftime('%B')) # exemplo 'December' -> mês
print(x.strftime('%m')) # exemplo '12' -> mês entre 01-12
print(x.strftime('%y')) # exemplo '18' -> Ano abreviado
print(x.strftime('%Y')) # exemplo '2018' -> Ano
print(x.strftime('%H')) # exemplo '17' -> Hora entre 00-23
print(x.strftime('%I')) # exemplo '05' -> Hora entre 00-12
print(x.strftime('%p')) # exemplo 'PM' -> AM/PM
