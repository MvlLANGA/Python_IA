lista_num = []

while True:
    valores = int(input("Digite alguns valores pra gente: "))
    if valores == 0:
        print("Programa encerrado")
        break

    lista_num.append(valores)
    print("Lista(ordem de inserção):" , lista_num)
    print("Lista (ordenada):" , sorted(lista_num))
    
    