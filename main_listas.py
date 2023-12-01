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


while True:
    aluno = str(input("Digite o nome do aluno: "))
    if aluno == "sair":
        break
    else:
        nota = float(input(f"Digite a nota de {aluno}: "))
        alunos.append([aluno, nota])

# ---------------------------------
maxNota = 0
nomeAluno = ""

for item_atual in alunos:
    if aluno[1] > float(maxNota):
        maxNota = float(item_atual[1])
        nomeAluno = str(item_atual[0])


ln(30)
print(nomeAluno, maxNota)
ln(30)