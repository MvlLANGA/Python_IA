import numpy as np

def somar_matrizes():
    try:
        m1 = np.array([6,23,18])
    
        m2 = np.array([18,9,17])
        soma= m1 + m2
        print(soma)
    except Exception as e:
        print(f"ERRO de soma {e}")
somar_matrizes()


# OU

def somar_matrizes(matriz1, matriz2):
    if np.shape(matriz1)== np.shape(matriz2):
        return matriz1 + matriz2
    else:
        return "Erro: As matrizes devem ter o mesmo tamanho"
    
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[9,6]])
print(somar_matrizes(m1,m2))