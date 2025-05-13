num = int(input("Digite um numero: "))
if num >=100 and num <= 1000:
    print("Esse numero é menor ou igual a 1000")
elif num < 100 and num > 10:
    print("Esse numero é menor que 1000 e menor que 100") 
elif num <= 10 :
    print("Esse numero é menor que 1000 menor que 100 e menor que 10")       
else:
    print("Numero Invalido")    