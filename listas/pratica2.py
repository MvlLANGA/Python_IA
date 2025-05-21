quantidade = int(input("Quantos numeros quer add: "))
lista_vazia =[]
contador= 0

while contador < quantidade:
    numero = int(input(f"Digite o {contador +1} numero: "))
    lista_vazia.append(numero)
    contador += 1

print("Lista final: ", lista_vazia)







