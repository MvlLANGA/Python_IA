pontos = int(input("Quantos pontos voce tem: "))
if pontos < 0:
    print("Impossivel")
elif pontos <= 49:
    print("Falhar")
elif pontos <= 59:
    print("1")
elif pontos <= 69:
    print("2")
elif pontos <= 79:
    print("3")
elif pontos <= 89:
    print("4")
elif pontos <= 100:
    print("5")
else:
    print("Impossivel")