ano = int(input("Escolha um ano: "))

if (ano %100 != 0 and ano %4 ==0) or ano %400 == 0:
    print("Ano Bissexto")
else:
    print("Não é ano bissexto")