valor = float(input("Total da conta: "))
gorjeta = float(input("Qual o valor da gorjeta: "))
total = valor + (valor * gorjeta/100)
print(f"O valor da conta: R${valor} \nA taxa de gorjeta: {gorjeta}% \nTotal da conta: R${total:.2f}")