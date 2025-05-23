lista_notas = []
aprovadas = []
# Enquanto tamanho da lista "lista_notas" for menor que 5 vai repetir while

while len(lista_notas) <5:
    #Input de entrada de usuario
    notas = int(input("Digite as notas: "))
    #Adiciona a nota do input na lista de notas
    lista_notas.append(notas)

    #If que verifica se a nota é maior que 6
    if notas >= 6:
        #adiciona a nota a uma nova lista se a nota for maior que 6
        aprovadas.append(notas)

 #Ao final do script, ele exibe as notas de aprovação maior que    
print(f"Notas de aprovação: {aprovadas}")



   


    
   



    
    
