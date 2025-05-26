def lista_compras():
    produtos =[]

    while True:
        print("1-Adicionar produtos")
        print("2-Remover")
        print("0-Sair")

        compras = input("Digite sua escolha: ")


        if compras == "0":
            print("--- Sua lista esta completa ---")
            break
        
        if compras == "1":
            escolha = input("Escolha o produto: ")
            produtos.append(escolha)
            print(produtos)
         
        if compras == "0":
            print("--- Sua lista esta completa ---")
            break

        if compras == "2":
            if escolha in produtos:
                item_remover = input("Qual item deseja remover: ")
                produtos.remove(item_remover)
                print(f"Item removido: {item_remover}")
        
        else:
            print(produtos)

    lista_ordenada = sorted(produtos)
    print("---Sua lista de produtos: ", lista_ordenada)
lista_compras()
            