import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes) #Usamos o read para ler o arquivo
#print(df_filmes) #Printamos a lista de filmes

#Head() e o Tail()
print("*Primeira 5 linhas do DataFrame")
print(df_filmes.head()) # Vai printar os 5 primeiros registros

#Tail()
print("\n *Ultimas 5 linhas do DataFrame de filmes:")
print(df_filmes.tail()) #Vai printar as 5 ultimas linhas

#Info()
print("\n *Informações sobre o DataFrame")
print(df_filmes.info())

#shaoe()
print(f"\nO dataframe de filmes tem {df_filmes.shape[0]} linhas e colunas {df_filmes.shape[1]}") #pedindo quantas linhas tem o dataframe[0]e o colunas[1]

#Describe
#Gera estatistica do data frame
print("Estatistica do DataFrame: ")
print(df_filmes.describe())

#Index
#Traz informações sobre osindices das linhas
print("Informações do Indice")
print(df_filmes.index)