import matplotlib.pyplot as plt
import numpy as np

#Grafico de linha
x=[1,2,3,4,5]
y=[2,5,6,8,6]

plt.plot(x,y)
plt.title('Exemplo de linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()

#Grafico de Barra
categorias = ['A', 'B', 'C']
valores =[10,2,30]
plt.bar(categorias, valores)
plt.title('Barras')
plt.show()

#Grafico de pizza
plt.pie(valores, labels = categorias, autopct='%1.1f%%')
plt.title('Pizza')
plt.show()

#Histograma
dados =np.random.randn(1000)
plt.hist(dados, bins=30)
plt.title('Histograma')
plt.show()

#Dispersão
x2 = np.random.rand(50)
y2 = x2 + np.random.randn(50)*0.1
plt.scatter(x2, y2)
plt.title('Dispersão')
plt.show()

#Usando metodo de seno do numpy
y-line = np.sin(x2)
categorias