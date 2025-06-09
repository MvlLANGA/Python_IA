import numpy as np #importamos a biblioteca numpy

def gerar_array_intervalo(): #criamos a função
    n1 = int(input("Escolha um numero: ")) #oedimos ao usuario o numero inicial
    n2 = int(input("Escolha outro numero: ")) #pedimos o numero final
    array_aleatorio = np.arange(n1, n2+1, 1) #chamamos o np.array pra saber os numeros inteiros no intervalo entre n1 a n2, o +1 serve pra add o ultimo numero
    print(array_aleatorio)
gerar_array_intervalo()