def ln(x):
    print("-"*x)

frutas = ["Maça","Banana","Goiaba","Pera","Limão"]
familia = ["Auridebson","Luciana","Guilherme","Levy"]
numeros = [22,34,66,92,74,19,90,98,32,35,61]

def pegaLista(lis):
    res = ""
    for item in lis:
        if enumerate(item) == True:
            res += item
        else:
            res += f'{item}\n'
    return res

ln(30)
print(pegaLista(numeros))
# for fruta in frutas:
#     print(fruta)
ln(30)