
frutas = ["banana", "maçã", "melão", "caju", "abacaxi"]
indice = len(frutas) # Usa o len pra entender o tamanho da lista
try:
    fruta = int(input(f"Escolha o indice de fruta entre 0 a {indice-1}: "))
    print(frutas[fruta])

except ValueError: # Aparece quando por engano digitamos uma letra na entrada
    print("ERRO: entrada errada, digite um indice correto")

except IndexError: # Aparece quando digitamos um valor de indice acima do desejado
    print("ERRO: Valor inelegivel")

else:
    print("*** Indice escolhido ***")

    

   