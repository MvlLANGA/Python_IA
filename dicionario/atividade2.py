def add_filme(database:list, nome:str, diretor:str, ano:int, duracao: int):
    filme = {
        "nome":nome,
        "diretor":diretor,
        "ano":ano,
        "tempo de execução":duracao
    }
    database.append(filme)
# Lista (banco de dados de filmes)
meus_filmes = []

print("-" * 60)
# Adicionando um filme
add_filme(meus_filmes,"Harry Potter","não sei direito",1998,169)

# Adicionar outro
add_filme(meus_filmes,"Anjos da Lei","não faço ideia",2014,178)

print(meus_filmes)
print("-" *60)


    