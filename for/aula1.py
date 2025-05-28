# Estudo de FOR


#lista = ["maria", "madalena", "pedro", "paulo", "alex"]
#for item in lista: # O que esta dentro do For vai ser executado no print
#    if len(item) > 2:
#        print(f"O item {item} tem mais de 2 caracteres")
#    else:
#        print(f"{item} tem menos de 2 caracteres")    


# Usando o Range no for

#for i in range(5): #Aqui usamos o range para limitar a quantidade de elementos que vai imprimir
#    print(i)


#for j in range(5,10): # Aqui ele mostra por onde ele vai começar(5) e aonde ele vai terminar no caso (10)
#    print(j)


#for h in range(0,10,2): #Aqui ele vai começar no (0) vai até o (10)< contando de dois em dois (2)
#    print(h)

# Criando uma lista a partir do range

#numero = list(range(3,15)) # Ajuda vc a criar uma lista usando o list(range) -- aqui ele pede uma lista de (3) a (15)
#print(numero) # caso vc queira um elemento da lista, voce coloca o [] e o numero do elemento EX: print(numero[5])

#for i in numero:
#    print(i)

# count() conta quantas vezes uma string ou inteiro tem dentro de um conjunto
#minha_string = "Quantas madeiras um esquilo pode empilhar se um um esquilo pudesse empilhar madeiras"
#print(minha_string.count("a"))

#minha_lista = [1,2,3,4,5,6,2,3,1]
#print(minha_lista.count(6))

#Replace ele ajuda a mudar um objeto dentro de uma variavel
#minha_palavra = "oi oi oi amigos"
#nova_palavra = minha_palavra.replace("oi", "ola")
#print(nova_palavra)