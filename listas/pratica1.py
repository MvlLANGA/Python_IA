num =[1,2,3,4,5]

while True:
    print("Lista atual", num)

    indice = int(input("Novo indice, caso digite -1 para o programa: "))
    
    if indice == -1:
        print("Programa encerrado")
        break

    if 0 <= indice < len(num):
        indice = int(input("Novo valor: "))
        num[indice] = indice
        
    
    else:
        print("Fim do Programa")
print("A lista atualizada: ", num)

    

    
           
  

    
        

    
