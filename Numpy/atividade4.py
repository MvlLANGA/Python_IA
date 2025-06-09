import numpy as np

def estatistica_array(array):
    soma = np.sum(array)
    media = np.mean(array)
    return soma , media
meu_array = np.array([15,36,12,7,24])
print(estatistica_array(meu_array))