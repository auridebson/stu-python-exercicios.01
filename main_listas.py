# Listas:

#ok Crie uma lista com os números de 1 a 10 e imprima-a.
#ok Adicione o número 11 à lista e imprima novamente.
#ok Remova o número 5 da lista e imprima o resultado.
#ok Crie uma segunda lista com os números de 11 a 15 e concatene-a à primeira lista.
#ok Imprima apenas os números pares da lista resultante.

import random
from arrays import *
print(num1a10)

num1a10.append(11)
print(num1a10)

num1a10.remove(5)
print(num1a10)

lista3 = num1a10+lista2
print(lista3)

for item in lista3:
    if item%2==0:
        listaPares.append(item)
print(listaPares)