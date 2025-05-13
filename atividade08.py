preco = float(input("Digite o preço do produto: "))
desconto =float(input("digite o desconto: "))
total = preco -(preco * desconto / 100)
print(f"O preço do produto é: {preco} \nCom desconto de {desconto}%\nO total é: {total :.2f}R$")