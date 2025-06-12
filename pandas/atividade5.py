import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes)

#Contando quantos filmes cada diretor dirigiu
contagem_diretores = df_filmes['Director'].value_counts()
print("\n **Os 10 diretores mais frequentes: ")
print(contagem_diretores.head())

#Ordenando os filmes pelo seu tempo de duração
df_filmes['Runtime'] = df_filmes['Runtime'].str.replace('min', '')
df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'], errors='coerce')
df_tempo_duracao = df_filmes.sort_values(by='Runtime', ascending=False)
print("\n **Top 10 filmes em tempo de duração: ")
print(df_tempo_duracao.head(10))

#Ordenando os filmes por 'certificado' em ordem alfabetica em seguida ordene decrescente 'Meta_score'
df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
df_ordenando_certificado = df_filmes.sort_values(by=['Certificate', 'Meta_score'], ascending=[True,False])
print("\n Top Ordenando Certificate e Meta_score: ")
print(df_ordenando_certificado.head())