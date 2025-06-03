try:
    num = int(input("Digite um numero Inteiro: "))

except ValueError:
    print("** ERRO: Entrada errada **")

except Exception as e:
    print(f"ERRO: Aconteceu um erro inesperado {e}")

else:
    print("** Obrigado pela sua Colaboração **")


