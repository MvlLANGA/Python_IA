tentativas = 0
while True:
    codigo = input("Digite seu PIN: ")
    tentativas += 1

    if codigo == "12345":
        sucesso = True
        break
    
    if tentativas == 3:
        sucesso = False
        break
    
    print("Incorreto...Tente novamente")
if sucesso:
    print("Pin correto Inserido")
else:
    print("BlOQUEADO")    