import mymodule as mx

mx.greeting('Jonathan')

# Módulos integrados
import platform

x = platform.system()
print(x)

# Listar todos os nomes de funções ou variáveis de um módulo
x = dir(platform)
print(x)

x = dir(mx)
print(x)
