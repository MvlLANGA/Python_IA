numeros = [30, 45, 22]
resultado = len(numeros)
try:
    num1 = int(input("Escolha um numero que seja divisivel por algum numero do indice: "))
    num2 = int(input(f"Escolha o indice desejado {resultado-1}: "))
    divisao = numeros[num2]/ num1
    print(f"A divisão {num1} por {num1} é: {divisao}")

except ValueError:
    print("ERRO: ** Entrada Invalida **")

except ZeroDivisionError:
    print("ERRO: ** Numero não pode ser dividido por ZERO **")

except Exception as e:
    print(f"Ocorreu um erro inesperado {e}")

else:
    print("** Operação realizada com sucesso **")
    
