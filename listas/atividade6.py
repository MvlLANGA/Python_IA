def eliminar_duplicatas():
    numeros =[]
    while len(numeros) <10:
        num = int(input(f"Digite o {len(numeros)+1} numeros: "))
        numeros.append(num)

    unicos = []
    repetidos = []
    i = 0
    while i < len(numeros):
        if numeros[i] not in unicos:
            unicos.append(numeros[i])
        else:
            repetidos.append(numeros[i])
        i += 1
    print("-" * 60)
    print("Numeros unicos: ", unicos)
    print("-" * 60)
    print("Numeros: ", numeros)
    print("-" * 60)
    print("Numeros Repetidos: ", repetidos)
    print("-" * 60)

eliminar_duplicatas()    
