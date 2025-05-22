# Criando listas
minha_lista = [10, 30, 15]
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])

# Trabalhando com elementos da lista
resultado = minha_lista[0] + minha_lista[2]
print(resultado)

# Tamanho da lista
tamanho_lista = len(minha_lista)
print(f"Minha lista tem {minha_lista} de tamanho.")

# mudando o valor de um indice
numero = [1, 2, 3, 4, 5]
numero[3] = 25
print(numero)

# Fatiar listas
letras = ["a", "b", "c", "d", "e"]
print(letras[1:4]) #Ele corta de 1 ao elemento de indice 4
print(letras[:3]) # Corta do inicio até o 3-1
print(letras[3:]) # Corta do indice 3 até o final
print(letras[::2]) # todos, com passo 2
print(letras[::-1]) # lista invertida

# Adicionar itens a lista
numeros =[]
numeros.append(5)
numeros.append(3)
numeros.append(10)



# adicionar itens em lugar especifico
numeros.insert(1,50)
numeros.insert(0,20)
numeros.insert(3,200)


# remover itens da lista pelo indice
numeros.pop(2)
numero_deletado = numeros.pop(0)
print(numero_deletado)

# remove o item pelo nome ou numero do proprio item
numeros.remove(200)
print(numeros)