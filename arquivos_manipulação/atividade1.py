def frutas():
    dicionario = {} # criamos um dicionario vazio pra receber ele no final do programa
    try:
        with open ("frutas.csv") as novo_arquivo:
            for linha in novo_arquivo:
                linha.replace("\n", "") # Tira o \n do final de cada linha
                if linha: # Elimina as linhas vazias
                    dados = linha.split(";") #Cada uma das linhas o splite vai transformar cada ; em uma lista
                    dicionario[dados[0]] = float(dados[1]) #dados[0] é a chave do nosso dicionario e o float vai ser o valor
    except FileNotFoundError:
        print("Arquivo Frutas.csv não encontrado")

    except ValueError:
        print("ERRO ao converter o preço float")
    return dicionario
print(frutas())




        
