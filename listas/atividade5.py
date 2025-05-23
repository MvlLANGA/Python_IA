lista_tarefas = []
def tarefas (minhas_tarefas):
    print("=== Tarefas ===")
    while True:
        print("1-Adicionar")
        print("2-Remover")
        print("3-Mostrar")
        print("4-Sair")
        print("-"* 30)

        menu = input("Escolha uma opção: ")


        if menu == "4":
            print("** Suas Tarefas diarias!! **")
            print(lista_tarefas)
            print("** Sair **")
            break

        if menu == "1":
            tarefa = input("Adicione uma tarefa: ")
            lista_tarefas.append(tarefa)
            print(lista_tarefas)
            print("** Tarefa Adicionada **")
    
        if menu == "2":
            lista_tarefas.pop()
            print(lista_tarefas)

        if menu == "3":
            print(f"Essa é a nossa lista total de tarefas ---{lista_tarefas}---")
            break

tarefas(lista_tarefas)

      