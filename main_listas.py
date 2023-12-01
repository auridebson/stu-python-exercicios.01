# Listas:

#ok Crie uma lista com os números de 1 a 10 e imprima-a.
#ok Adicione o número 11 à lista e imprima novamente.
#ok Remova o número 5 da lista e imprima o resultado.
#ok Crie uma segunda lista com os números de 11 a 15 e concatene-a à primeira lista.
#ok Imprima apenas os números pares da lista resultante.

import random
from arrays import *

# ln(40)
# print("Alimente uma lista de frutas\nAdicione uma fruta por vez e para sair digite SAIR.")
# ln(40)

# while True:
#     entrada = input("Digite um fruta: ")
#     if entrada == "sair":
#         break
#     else:
#         frutas.append(entrada)

# ln(30)
# for indice, fruta in enumerate(frutas):
#     print(f"{indice+1}ª Fruta - {fruta}")
# ln(30)

    # "nome":"",
    # "cor":"",
    # "raca":"",
    # "adestrado":False,
    # "idade":"",

nome = input("Digite o nome do gato: ")
gato["nome"] = nome
gato["cor"] = str(input(f"Digite a cor do gato {nome}: "))
gato["raca"] = input(f"Digite a raça do {nome}: ")
gato["idade"] = int(input(f"Digite a idade de {nome}: "))
gato["vacinado"] = bool(input("Vacinado? "))

print(gato)

ln(30)
print(" - ")
ln(30)