lista = []


while True:
    resposta =input("Qual a opção escolhida: ")

    if resposta == "+":
        if len(lista) == 0:
            lista.append(1)
        else: 
            lista.append(lista[-1] +1)
    else:
        if len(lista) == 0:
            print("A lista esta vazia")
        else:
            lista.pop(len(lista) -1)

    print(lista)

        

       

