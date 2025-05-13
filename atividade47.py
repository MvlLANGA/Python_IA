#primeira variavel
limite_sup = int(input("Escolha um numero: "))
#variavel complementar
lim = 1
#usando while com as duas variaveis
while lim <= limite_sup:
    print(lim)
#aqui usamos a variavel complementar pra fazer a multiplicação
    lim *= 2
print("Esse é o limite superior", limite_sup)
