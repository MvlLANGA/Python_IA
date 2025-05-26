import re

lista_senhas = []

def minhas_senhas():
    lista_senhas = []
    while len(lista_senhas)< 5:
        senha = input(f"Digite a {len(lista_senhas)+1} senha: ") 
        

        if len(senha) >= 8 and re.search("[0-9]", senha) != None: 
           lista_senhas.append(senha)
    
        else:    
            
            print("Senha Invalida!! Deve ter pelo menos 8 caracteres e conter um numero")
    
    print("senhas validas:")
    i =0

    while i < len(lista_senhas):
        print(lista_senhas[i])
        i +=1

minhas_senhas()