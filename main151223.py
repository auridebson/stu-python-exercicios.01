def ln(x):
    print("-"*x)

frutas = ["Maça","Banana","Goiaba","Pera","Limão"]
familia = ["Auridebson","Luciana","Guilherme","Levy"]
numeros = [22,34,66,92,74,19,90,98,32,35,61]
palavra = ["p","y","t","h","o","n"]

def pegaLista(lis):
    maior_nota = lis[0]
    for nota_atual in lis:
        if  nota_atual > maior_nota:
            maior_nota = nota_atual
    return maior_nota

ln(30)
print(pegaLista(numeros))
ln(30)


