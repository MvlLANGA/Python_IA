def lista():
    lista_telefonica ={}
    while True:
        print("--- MENU ---")
        print("1- Busca")
        print("2- Adiciona")
        print("3- Sair")

        comando = input("Escolha o comando que você deseja (1 busca. 2 adiciona. 3 sair.): ")
        print(f"Ok!! Comando: {comando} ")


        if comando == "1":
            nome = input("Escolha o nome: ")
            if nome in lista_telefonica:
                print(f"Nome: {nome} \nTelefone: {lista_telefonica[nome]} ")
                i =0
                while i < len(lista_telefonica[nome]):
                    print(lista_telefonica[nome][i])
                    i += 1
            else:
                print("Nome não encontrado")

        elif comando == "2":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            if nome in lista_telefonica:
                lista_telefonica[nome].append(telefone)
                print("Novo contato adicionado com sucesso")
            else:
                lista_telefonica[nome] = [telefone]
            print("Novo contato adicionado com sucesso!")


        elif comando == "3":
            print("Saindo do Programa")
            print(lista_telefonica)
            break

        else:
            print("Comando Invalido!! Tente novamente>")

lista()
