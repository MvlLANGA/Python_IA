import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes) #Usamos o read para ler o arquivo
#print(df_filmes) #Printamos a lista de filmes

#Criando uma nova coluna chamada 'Rating_Metascore_Diff' com a diferença
#entre 'Rating' e ('Metascore/10)
df_filmes['Rating_Metascore_Diff'] = df_filmes['IMDB_Rating'] - (df_filmes['Meta_score']/10)
print("\n O DataFrame agora tem uma nova coluna: ")
print(df_filmes.head())

#Mostrando colunas Titulos/Rating/Metascore
colunas_mostradas = df_filmes[['Series_Title', 'IMDB_Rating','Rating_Metascore_Diff']]
print("\nMostrando as colunas: Titulo, Rating e ano dos primeiro 5 filmes: ")
print(colunas_mostradas.head())

#excluindo coluna Overview e copiando dataframe original
copiando = df_filmes.copy()
print(copiando)
df_filmes = df_filmes.drop('Overview', axis=1)
print("\n colunas apóes remoção da descrição: ")
print(df_filmes.head())

#Renomeando a coluna 'Votes' 
# Renomeando a coluna 'coluna_antiga' para 'coluna_nova' usando inplace=True
df_filmes.rename(columns={'No_of_Votes': 'Numero_votos'}, inplace=True)
print("\nDepois de renomear:")
print(df_filmes.head())





