import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes) #Usamos o read para ler o arquivo

#seleciona apenas as colunas desejadas e mostra as 5 primeiras linhas
colunas_selecionadas = df_filmes[['Series_Title', 'Director','Released_Year']]
print("1. Titulo, Diretor e ano dos primeiro 5 filmes: ")
print(colunas_selecionadas.head())

#seleciona da linha 10 até a 15 ( inclusive da linha 16) e cioluna 0 a 3
sub_conjunto_iloc = df_filmes.iloc[10:16, 0:4]
print("\n2. Linhas 10 a 15 e colunas 0 a 3 com iloc: ")
print(sub_conjunto_iloc)

#cria uma copia do dataframe com a coluna 'IMDB_Rating com indice ( sem alterar o original)
df_temp = df_filmes.set_index('IMDB_Rating')

#seleciona os filmes de RANK 1 a 5 e mostra apenas o 'TITLE' e "Revenue" (MILLIONS)
print("\n3. Filmes de Rank de 1 a5 com Receita: ")
print(df_temp[['Series_Title', 'Gross']].head())


#Converte a coluna 'Released_Year' para numerico, caso ainda não esteja
df_filmes['Released_Yar'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce') #Esse esse errors para caso tenha numeros invalidos não de erro ou não tenha dados

#filtra os filmes com ano >= 2016"
filmes_pos_2016 = df_filmes[df_filmes['Released_Year'] >= "2016"][['Series_Title', 'Released_Year']]
print("\n4. Filmes lançados a partir de 2016: ")
print(filmes_pos_2016)