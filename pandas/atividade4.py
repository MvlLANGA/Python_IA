import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" #importamos o DF copiando o nome junto com o csv
df_filmes = pd.read_csv(url_filmes) #Usamos o read para ler o arquivo
#print(df_filmes) #Printamos a lista de filmes

#Verificando os valores ausentes nas colunas "Revenue(Millions)" e "Metascore" do df_filme original
df_filmes1 = df_filmes[['Gross', 'Meta_score']]
print("\n Contagem de valores ausentes por coluna: ")
print(df_filmes1.isna().sum())

#criando um DataFrame chamado df_filmes_completo
df_filmes_completo = df_filmes.copy()
print(df_filmes_completo)

#removendo rodas as linhas que contenham qualquer valor nan
df_filmes_completo.dropna(inplace=True) #Exclui as linhas e registros que tem dados ausentes
print(f"Numero de linhas do DataFrame original: {len(df_filmes)}")
print(f"Valores depois do drop: {len(df_filmes_completo)}")

# Garantindo que as colunas estão numéricas
df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
df_filmes_completo['Gross'] = pd.to_numeric(df_filmes_completo['Gross'], errors='coerce')
df_filmes_completo['Meta_score'] = pd.to_numeric(df_filmes_completo['Meta_score'], errors='coerce')
print(df_filmes_completo['Gross'])

#Preenchendo os Nans
#Criando uma copia do DataFrame original
df_filmes_preenchido_media = df_filmes_completo.copy()
df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].mean())
#verificando se ainda existem NaNs colunas
print("\nValores ausentes após preenchimento: ")
print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum)
