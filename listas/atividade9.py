def lista_crescente():
    lista_numero = []


    while True:
        num = int(input("Digite alguns numeros em ordem decrescente: "))
        lista_numero.append(num)

        if len(lista_numero) > 1 and lista_numero[-1] < lista_numero[-2]:
            break
    
    numeros_ordenados = sorted(lista_numero)
    print("Numeros digitados (ordem crescente): ", numeros_ordenados)

lista_crescente()