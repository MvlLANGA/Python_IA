texto = input("Escolha um texto: ")
try:
    with open("saida.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto)
        print("Texto salvo com sucesso!!")

except FileNotFoundError:
    print("ERRO: Essse arquivo ja existe.")