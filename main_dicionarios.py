from arrays import *

# Dicionários:

#ok Crie um dicionário com três chaves representando nomes de pessoas e seus respectivos anos de nascimento.
#ok Adicione uma nova pessoa ao dicionário.
#ok Remova uma pessoa do dicionário.
#ok Imprima apenas as chaves do dicionário.
# Imprima apenas os valores do dicionário.


for membro in familia:
    print(f"{membro} - {familia[membro]}")
ln(30)

familia['alicia'] = 2021
print(familia)
ln(30)

# Removendo um item do dicionário
del familia["tobby"]
print(familia)
ln(30)

# Imprimindo só as chaves
for membro in familia:
    print(membro)
ln(30)

# Imprimindo só os valores
for membro in familia:
    print(familia[membro])
ln(30)
