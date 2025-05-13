senha = input("Digite uma senha: ")
while True:
    senha2 = input("Digite a senha novamente: ")
    if senha != senha2:
        print("ACESSO NEGADO!!! -Tente novamente")
    else:
        print("** Acesso permitido **")
        break
