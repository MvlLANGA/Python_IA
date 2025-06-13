import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Criando um DF de exemplo

df = pd.DataFrame({
    'filme': ['A', 'B','C', 'D', 'E'],
    'nota' : [8.5,9.5,7,6.8,5],
    'receita': [120,80,150,50,60]
})

#Grafico de Barras com colunas do Frame
plt.bar(df['filme'], df['nota'])
plt.title('Notas por filme')
plt.ylabel('Nota')
plt.show()