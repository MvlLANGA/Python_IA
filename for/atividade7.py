mesa = [
    ["","",""],
    ["","",""],
    ["","",""] 
    ]
contador = 0
print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
def jogue_o_jogo(mesa,linha,coluna,caracter):
    mesa[linha][coluna] = caracter
    exibe_resultado()
    if contador % 2 != 0:
        jogador = "1 (x)"
    else:
        jogador = "2 (O)"
       
    print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
    print("")
 
def exibe_resultado():
    for linhas in mesa:
        for items in linhas:
            if items == "":
                print("_ ",end="")
            print(items,end=" ")
 
        print(" ")
   
while True:
    linha = int(input("Qual a linha: "))
    coluna = int(input("Qual a coluna: "))
    caracter = input("Qual o caracter: ")
    jogue_o_jogo(mesa,linha, coluna, caracter)
    contador += 1
    if contador == 9:
        exibe_resultado()
        break
    