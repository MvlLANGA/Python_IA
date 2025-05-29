#dicionario

#Usado para armazenar dados em formato chave e valor
#São oredenados
#mutaveis
#não permite elementos duplicados.

meu_dicionario = {}
meu_dicionario["apina"] = "macaco" # aqui colocamos a cahave [] e o valor da chave ""
meu_dicionario["nome"] = "marcos"
#print(meu_dicionario)
#print(meu_dicionario["nome"])

palavra = input("Digite uma palavra: ")
if palavra in meu_dicionario:
    print("Tradução: ", meu_dicionario[palavra])
else:
    print("Palavra não encontrada")