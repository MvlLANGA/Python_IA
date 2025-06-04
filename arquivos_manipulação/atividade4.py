with open("texto.txt") as arquivo:
    linhas = 0
    for linha in arquivo:
        linhas +=1
    print(linhas)