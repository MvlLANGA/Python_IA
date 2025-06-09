import pandas as pd 

# criando uma série
#idade_nome = pd.Series([1,2,3,4], index = ['Ana', 'João', 'Paula', 'Andre']) #colocamos Series em letra maiuscula o S.
#print(idade_nome)                 #Index quer dizer indice

#Data Frame ou df
dados_alunos = {
    'nome':['Ana', 'João', 'Paula', 'Andre'],
    'idade':[1,2,3,5],
    'curso':['Engenharia', 'Ciencias', 'Biologia', 'Direito']

}
df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)