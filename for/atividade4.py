lista = [2,3,7,8,10,12,18,13,14]

def numero_pares(pares):
    new_lista = [] 
    for par in lista:
        if par % 2 == 0:
            new_lista.append(par)
    return new_lista
        
print(numero_pares(lista))
