import numpy as np
print("-" *80)
arr1d = np.array([7,6,9,3,4,2]) 
print(f"O arr1d é: {arr1d}, Dimensões: {arr1d.ndim}, shape: {arr1d.shape}, dtype: {arr1d.dtype}, bytes: {arr1d.itemsize}")

print("-" *80)
arr2d_float = np.array([[4.1,6.3,9.9],[8.5,7.4,5.3]])
print(f"O arr2d é: {arr2d_float}, Dimensões: {arr2d_float.ndim}, shape: {arr2d_float.shape}, dtype: {arr2d_float.dtype}, bytes: {arr2d_float.itemsize}")
print("-" *80)