#dicionario

#Usado para armazenar dados em formato chave e valor
#São oredenados
#mutaveis
#não permite elementos duplicados.

#meu_dicionario = {}
#meu_dicionario["apina"] = "macaco" # aqui colocamos a cahave [] e o valor da chave ""
#meu_dicionario["nome"] = "marcos"
#print(meu_dicionario)
#print(meu_dicionario["nome"])

#palavra = input("Digite uma palavra: ")
#if palavra in meu_dicionario:
#    print("Tradução: ", meu_dicionario[palavra])
#else:
#    print("Palavra não encontrada")


#resultado = {}
#resultado["maria"] = 5
#resultado["julia"] = 10


#soma = resultado["maria"] + resultado["julia"]
#print(soma)

#dicionario ={}

#dicionario["apina"]= "macaco"
#dicionario["banana"]= "amarela"
#dicionario["cembalo"]= "cravo"

#for chave in dicionario:
#    print("chave: ", chave) # aqui ele vai printar primeiro o valor da chave
#    print("valor: ", dicionario[chave]) # aqui vai printar a chave e o valor da chave 


#popular

#lista_palavras = [
#  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
#]

#def contagens(minha_lista):
#    palavras = {} # "chave: " "valor"
#    for palavra in minha_lista: # para palavra esta em minha_lista
#        if palavra not in palavras: # se palavra esta dentro do dicionario palavras
#            palavras[palavra] = 0 

#        palavras[palavra] += 1 #abrimos um contador para cada palavra ja existente
#    return palavras #retorna o dicionario palavras
#print(contagens(lista_palavras))