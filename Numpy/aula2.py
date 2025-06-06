import numpy as np
#Aqui é uma variavel que representa o metodo default_rng
rng = np.random.default_rng()

#Criar array a partir de listas e tuplas
lista_py = [5, 9, 2, 3, 6]
print(lista_py)
array_1d = np.array(lista_py) #melhor pra trabalhar com biblioteca fica sempre mais rapido
print(array_1d)

lista2_py = [[1,2,3,4],[1,2,3,4]]
array_2d = np.array(lista2_py)
print(array_2d)


tupla =(1,2,3,4,5,6,7,8,9,10) # não pode ser modificada
array_tupla = np.array(tupla) # O np.array transforma as listas e as tuplas em um arranjo(array)
print(array_tupla)

#npzeros
#cria um array preenchido por zeros
zero_array = np.zeros((3,3), int)# o INT transforma em numeros inteiros tirando o ponto na saida # 3 numero de linhas e 3 numero de colunas
print(f"Array de zero:\n {zero_array}")

#np.ones
one_array = np.ones((2,3), int)
print(one_array) #O ones faz sair uma matriz 2x3 tudo com numero1

#np.full
#cria um array preenchido com numeros especificos
full_array = np.full((2,4), 7.5)
print(full_array)

#np arange
array_arange = np.arange(0,10,2) #Ele conta de 2 em 2 de 0 a 10
print(array_arange)

arra_float_arange = np.arange(0.0, 1.0, 0.25) # ele conta de 0.25 em 0.25 de 0 ate 1.0
print(arra_float_arange)

#Array de numeros aleatorios
array_aleatorios = rng.random((2,5))
print(array_aleatorios)
#O intergers escolhe numeros aleatorios nessa caso de 0 a 1000 escolhendo 10 numero(size=10)
array_aleatorios = rng.integers(0, 100, size=10)
print(array_aleatorios)

#indices em numpy
#indice vetor
array_indice = np.array([1,2,5,9,8])
print(f"O lemento 0: {array_indice[0]}")
print(f"O lemento 3: {array_indice[3]}")

#indice Matriz
array_indice_matriz = np.array([[1,2,4,5,6],[5,6,7,0,3]])
print(f"Elemento na linha 0, coluna 2: {array_indice_matriz[0,2]}") #Aqui pedimos o elemento da linha 0 e coluna 2 no caso numero 4

#Slicing
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 12, 13],
                  [14, 7, 15, 16]])
fatia2d_a = arr2d[:2, 1:3] #fatia em 2 colunas da linha 1 e os elementos 1 ao 3
print(fatia2d_a)           # O : voce usa pra fatiar 
#saida:
#[[2,3]]
#[6,12]]

#operaçoes matematicas
#adição
array_a = np.array([1,3,5,8])
array_b = np.array([2,3,4,5])
soma = array_a + array_b
print(soma)

#subtração
menos = array_a - array_b
print(menos)

#multiplicação
vezes = array_a * array_b
print(vezes)

#divisão
divisao = array_a / array_b
print(divisao)

#Copy e View
precos = np.array([150.00, 10.99, 20.50])
print(f"Precos: {precos}")

precos_ajustados = precos # esse metodo e os precos ajustados com view é a mesma coisa
print(precos[0]*2)
#precos_ajustados = precos.view() #somente espelha nesse caso o precos_ajustados

preco_ajustado2 = precos.copy() # o copy copia os valores de precos
print(preco_ajustado2)

#iteração
array = np.array([1,2,3,4,5,6,7,8,9])

for n in array:
    print(f"valor: {n}")