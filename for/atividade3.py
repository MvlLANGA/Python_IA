inteiros = [2,7,6,-2,-3]


def soma_positivos(lista):
    soma =0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma
print(soma_positivos(inteiros))
    
        