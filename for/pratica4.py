lista_bidimensional = [
    [0,1,2,3],
    [0,8,6,3],
    [2,3,5,7],
    [5,9,7,4]]

num =0
def conta_elementos_match(lista, numero):
    contagem =0
    for i in lista:
        contagem += i.count(numero)
    return contagem

print(conta_elementos_match(lista_bidimensional,num))

    

