import pandas as pd

netflix_url = "netflix_titles.csv"
df_netflix = pd.read_csv(netflix_url)
print(df_netflix)
print("-- As 5 primeiras linhas desse DataFrame são: ")
print(df_netflix.head())
print("\nOs dados e valores desse DataFrame são: ")
print(df_netflix.info())
print(f"O total de filmes é: {df_netflix.shape[0]} \nE suas caracteristicas são: {df_netflix.shape[1]}")
print(f"-- A nota média dos filmes é: {df_netflix.describe()}")