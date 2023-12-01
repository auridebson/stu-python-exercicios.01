# Listas:

#ok Crie uma lista com os números de 1 a 10 e imprima-a.
#ok Adicione o número 11 à lista e imprima novamente.
#ok Remova o número 5 da lista e imprima o resultado.
#ok Crie uma segunda lista com os números de 11 a 15 e concatene-a à primeira lista.
#ok Imprima apenas os números pares da lista resultante.

import random
from arrays import *

while True:
    entrada = input("Digite um fruta: ")
    if entrada == "sair":
        break
    else:
        frutas.append(entrada)

ln(30)

for fruta in frutas:
    print(fruta)