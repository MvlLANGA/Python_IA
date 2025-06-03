try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    divisao = num1 / num2
    print(f" A divisão de {num1} por {num2} é: {divisao}")

except ValueError:
    print("ERRO: Entrada errada!!")

except ZeroDivisionError:
    print("ERRO: Esse numero não pode ser dividido por ZERO!!")

except Exception as e:
   print(f"Ocorreu um erro inesperado {e}")

else:
    print("Divisão Feita")