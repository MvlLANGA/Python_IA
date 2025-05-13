idade = int(input("Qual sua idade: "))
if idade > 5 and idade < 100:
    print(f"Ok, Voce tem {idade}")
elif idade < 5 and idade > 0:
    print("Suspeito que voce esteja mexendo em um Pc.")
else:
    print("Isso deve ser um erro!!")