# #try:
# # aqui chamamos o arquivo pedimos para abrir como um novo arquivo e fechar
# #    with open("exemplo.txt") as novo_arquivo:
#     #    conteudo = novo_arquivo.read()
#         #print(conteudo)
#         for linha in novo_arquivo: # Esse for é para sair linha por linha no print
#             print(linha)
# except FileNotFoundError: # Tratamento de erro para Arquivo não encontrado!!
#     print("Não encontramos o arquivo")


#with open("pessoas.csv") as novo_arquivo:
#    for linha in novo_arquivo:
#        linha = linha.replace("\n","")
#        partes = linha.split(";")
#        nome = partes[0]
#        notas = partes[1:]
#        print("Nome: ", nome)
#        print("Nota: ", notas)

#with open("exemplo.txt") as arquivo:
#    f = arquivo.readline() # Le apenas uma unica linha do arquivo
#    #f = arquivo.readlines() # Le varias linhas
#    print(f[2])

#with open("exemplo.txt", "x") as arquivo: # O "a" é o append voce add uma nova linha
#    f = arquivo                           # O "w" apaga todas as linhas deixa somente a que vc escreveu
#                                          # O "x" cria um novo arquivo
#    f.write("\nNova linha, Jesus!!!")     # O "r" Le o arquivo