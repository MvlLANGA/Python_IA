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

#Criar uma nova coluna
df_filmes['Rating_x_10'] = df_filmes['IMDB_Rating']*10
print("\n O DataFrame agora tem uma nova coluna: ")
print(df_filmes.head())

#Conversão de coluna Gross para float e ignorando erros caso falhar
df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')

#agora, convertido o numero Gross em numero, é mais seguro fazer a comparação
df_filmes['Alta_receita'] = df_filmes['Gross'] > 1000
print("\n DataFrame com nova coluna 'Alta Receita' (Primeiras linhas)")
print(df_filmes.head())

#Drop
#Metodo drop remove uma linha (registro) ou coluna
#axis=1 - Exclui a coluna
df_filmes = df_filmes.drop('Poster_Link', axis=1)
print(df_filmes.head())

#axis = 0 - exclui o registro
df_filmes = df_filmes.drop(4, axis=0)
print(df_filmes.head())

#Limpando dados ausentes
#Verificar dados ausentes com .isna() .sum():
print("\n Contagem de valores ausentes por coluna: ")
print(df_filmes.isna().sum())

#Removendo linhas/colunas
#Criando uma copia para não
df_sem_nan_linhas = df_filmes.copy()

#removendo rodas as linhas que contenham qualquer valor nan
df_sem_nan_linhas.dropna(inplace=True) #Exclui as linhas e registros que tem dados ausentes
print(f"\n Numero de linhas original: {len(df_filmes)}")
print(f"\n Numero de linhas após drop: {len(df_sem_nan_linhas)}")

#Removendo colunas que tenham qualquer valor nan
df_sem_nan_linhas = df_filmes.dropna(axis=1)
print(f"Colunas originais: {df_filmes.columns.tolist()}") #printa as colunas antes do filtro
print(f"Colunas após dropna: {df_sem_nan_linhas.columns.tolist()}") #printa depois do filtro

#contando as frequencias de coluna
contagem_diretores = df_filmes['Director'].value_counts()#contando os diretores mais frequentes na lista
print("\n Os 10 diretores mais frequentes: ")
print(contagem_diretores.head(10))

#ordenando os filmes
df_ordenando_por_nota = df_filmes.sort_values(by='IMDB_Rating', ascending=False)
print("\n Top 5 filmes por nota (IMDB_Rating): ")
print(df_ordenando_por_nota.head())

#ordenando os filmes por mais de uma coluna
df_ordenando_por_nota = df_filmes.sort_values(by=['Released_Year', 'Gross'], ascending=False)
print("\n Top 5 filmes por ano e Gross: ")
print(df_ordenando_por_nota.head())

#Converter caso necessario
df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
df_filmes['IMDB_Rating'] = pd.to_numeric(df_filmes['IMDB_Rating'], errors='coerce')

df_filmes['IMDB_Rating'] = pd.to_numeric(df_filmes['IMDB_Rating'], errors='coerce')
#Calculando a média de IMDB e GROSS para cada REleased_year
metricas_por_ano = df_filmes.groupby('Released_Year').agg(
    Media_Rating =('IMDB_Rating', 'mean'),
    Media_Receita =('Gross', 'mean'),
    Total_filmes =('Series_Title', 'count'),
)
print(metricas_por_ano)

#Salvando em um arquivo csv sem o indice
df_filmes.to_csv('meus_filmes_bem_avaliados.csv', index=False)
print("\nDataframe salvo em Meus_filmes_bem_avaliados.csv")