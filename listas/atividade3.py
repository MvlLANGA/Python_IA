def nomes_unicos():
    lista_nome =[]

    while len(lista_nome) < 5:
        nome = input("Escolha um nome: ")
        
        if nome in lista_nome: #Verifica se o valor nome ja esta dentro da lista
            print("Esse nome não pode ser add novamente!!")
            
        else:
            lista_nome.append(nome)
        print(lista_nome)
nomes_unicos()
            

