senha1 = "4321"
tentativa =0
while True:
    senha2 = input("Digite a senha: ")
    
    if senha1 != senha2:
        print("Senha Incorreta")
        sucesso = False
        tentativa +=1
        print(f"Já foram {tentativa} tentativas")

    if senha1 == senha2:
        print("BEM - VINDO -- PIN CORRETO")
        sucesso = True
        
        break

