operacao1 = "adicao"
operacao2 = "subtracao"
operacao3 = "multiplicacao"
operacao4 = "divisao"
num1 = int(input("Adicione o primeiro numero: "))
num2 = int(input("Adicione o segundo numero: "))
operacao = input("Escolha uma operação matematica: ")
if operacao == "adicao":
    total_adicao = num1 + num2
    print(total_adicao)
elif operacao == "Subtracao":
    total_subtracao = num1 - num2
    print(total_subtracao)
elif operacao == "multiplicacao":
    total_multiplicacao = num1 * num2
    print(total_multiplicacao)
elif operacao == "divisao":
    total_divisao = num1 / num2
    print(total_divisao)
else:
    print("---ERROR---")    

