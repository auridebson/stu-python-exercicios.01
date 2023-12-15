# frase = lambda texto : texto.lower()

# minhaFrase = input("Digite seu texto: ")

# print(frase(minhaFrase))

# -----------------------------------

# menu = int(input("Escolha uma opção para fazer os cálculos:\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Potencialização\n"))

# entrada = int(input("Digite um número inteiro: "))
# numero = lambda entrada : "Número par" if (entrada % 2 == 0) else "Número ímpar"

# print(numero(entrada))

semaforo = input("Digite a cor do semaforo: ")

acao = lambda agir : "Parar" if semaforo == "vermelho" else "Siga" if semaforo == "verde" else "Acelere" if semaforo == "amarelo"

print(acao(semaforo))