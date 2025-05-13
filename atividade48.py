#Aqui temos que escolher a base de multiplicação
#primeira variavel
limite_sup= int(input("Escolha um numero: "))
base = int(input("Insira o numero de base maior que 1: "))
#variavel complementar
lim = 1
#usando while com as duas variaveis
while lim <= limite_sup:
    print(lim)
#aqui usamos a variavel complementar pra fazer a multiplicação
    lim *= base
print("Esse é o limite superior", limite_sup)