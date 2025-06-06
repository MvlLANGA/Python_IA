import numpy as np
def matriz_identidade():
    numero = int(input("escolha um numero para matriz: "))
    return np.identity(numero)
print(matriz_identidade())

