with open("dados.csv") as entrada:
    linhas =  entrada.readlines()
    maiores = []
    for linha in linhas:
        nome, idade = linha.strip().split(",")
        if idade >= 18:
            maiores.append(linha)
with open("dados_maiores.csv", "w") as saida:
    saida.writelines(maiores)
    print("Arquivo 'dados_maiores' criado com sucesso!!")