import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes) #Usamos o read para ler o arquivo
#print(df_filmes) #Printamos a lista de filmes


#selecionando a coluna "Title"
titulos_filmes = df_filmes['Series_Title']
print("Primeiros 5 Titulos")
print(titulos_filmes.head())

#selecionando multiplas colunas
filmes_selecionados = df_filmes[['Series_Title', 'Genre', 'IMDB_Rating']]
print(f"\n** DataFrame com titulo -- Genero e Nota")
print(filmes_selecionados.head())


#selecionando a primeira linha(registros)
#Iloc é usado para selecionar linhas por indeice numerico
primeiro_filme = df_filmes.iloc[200] #linha 200
print("\n Primeiro filme (Linha completa): ")
print(primeiro_filme)

#selecione as 3 primeiras linhas
tres_primeiros_filmes = df_filmes.iloc[0:3] #fatiamos pra pegar os indices 0 e 3
print("\nTres primeiros filmes (DataFrame): ")
print(tres_primeiros_filmes)

#selecionando linhas e colunas especificas
selecao_especifica = df_filmes.iloc[[0,3], [5,6]]
print("\n Printando uma seleção especifica, linha 0 e 3  e coluna 5, e 6")
print(selecao_especifica)

#Selecionando Dados com .loc
#localiza os dados pelos rotulos

df_filmes_idx = df_filmes.set_index("Series_Title")
print("\n Definimos o indice agora como Series Titles") #Aqui redefinimos o indice com os nomes dos filmes
print(df_filmes_idx.head())

Poderoso = df_filmes_idx.loc["The Godfather"] #Aqui selecionamos o filme e printamos todos os seus dados
print("\nDados do filme: The Godfather: ")
print(Poderoso)


#Filtrar os dados baseados em condições (Boolean indexing)
#Aqui pedimos os filmes com notas menores que 8.5
df_filmes_bem_avaliados= df_filmes[df_filmes['IMDB_Rating'] < 8.5]
print("n\Filmrs com nota >= 8.5 (Primeiras linhas)")
print(df_filmes_bem_avaliados[['Series_Title', 'Genre']].head())

#Filmes que tem genero 'Action'
#aqui selecionamos os filmes do genero ação
filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)] #o (na) serve pra registros que não genero para nao dar erro
print("\n Filmes que contem o genero 'Action'")
print(filmes_acao[['Series_Title', 'Genre']].head())