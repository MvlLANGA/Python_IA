lista_produtos = ["arroz", "feijao", "carne", "batata", "tomate"]


def produtos ():

    while True:
        nome = input("Digite o nome do produto ou -sair- para sair do programa: ")

        if nome == "sair":
            print("--- Até Mais---")
            break

        if nome in lista_produtos:
            print("=== Esse produto ja foi colocado na lista!! ===")

        else:
            print("=== Esse produto não esta na lista!!! ===")


produtos()
