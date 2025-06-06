import numpy as np

#saida do array e as dimensões pelo metodo(ndim)
arr1d = np.array([1,2,3])
print(f"Array 1d: {arr1d}, Dimensões: {arr1d.ndim}")

arr2d = np.array([[1,2,3,4,5], [5,6,8,9,6]])
print(f"Array 2d: {arr2d}, Dimensões: {arr2d}")

arr3d = np.array([[[0,5,6], [5,8,9]], [[4,5,6], [5,9,8]]])
print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}") #ndim; pega as dimensões do array

#shape
#Indica o tamanho do array

print(f"Shape do arr1d: {arr1d.shape}")
print(f"Shape do arr2d: {arr2d.shape}")
print(f"Shape do arr3d: {arr3d.shape}")

#Dtype
array_float = np.array([1.5,1.8, 9.5])
print(f"O dtype dessa array é: {array_float.dtype}") 
print(f"O dtype da arr1d é: {arr1d.dtype}") #dtype; pega o tipo de dado arranjo

#Itemsize
print(f"O itemsize do arr1d é: {arr1d.itemsize}")
print(f"O itemsize do arr3d é: {arr3d.itemsize}")
print(f"O itemsize di array_float é: {array_float.itemsize}") # inetmsize; amanho da lista em bites que consome