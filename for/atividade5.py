n1 = [4,8,9,10,11,28,2]
n2 = [7,6,2,3,7,6,13]

def lista_soma(lista1, lista2):
    soma = []
    for i in range(len(lista1)):
        resultado = lista1[i] +lista2[i]
        soma.append(resultado)
    return soma

print(lista_soma(n1, n2))
