nome = input("Digite o nome: ")
if nome != "jerry":
    porcoes = int(input("Digite o numero de porcoes: "))
    total = porcoes * 5.90
    print(f"O total da sua Conta: R${total:.2f}")
else:
    print("***Não Cadastrado***")