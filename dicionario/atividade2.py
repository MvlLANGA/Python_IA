def add_filme(database:list, nome:str, diretor:str, ano:int, duracao: int):

#criamos um dicionario chamado filmes, que pede nome:, diretor:, ano; e tempo de duração do film

   filme = {
        "nome":nome, #Para cada chave colocamos um valor EX "nome" essa é a chave nome, esse é o valor.
        "diretor":diretor,
        "ano":ano,
        "tempo de execução":duracao
    }
   database.append(filme)
# Lista vazia (banco de dados de filmes)
meus_filmes = []

#coleta de dados
print("Cadastro de Filme")

while True:
    nome = input("Digite o filme escolhido: ")
    diretor = input("Digite o nome do diretor: ")
    ano = int(input("Digite o ano do lançamento: "))
    duracao = int(input("Digite a duração em minutos: "))
    print("-" * 60)

# Adicionando um filme
    add_filme(meus_filmes, nome, diretor, ano, duracao)

# Aqui criamos um laço de repetição que so para quando o usuario escolhe não continuar 
    continuar = input("Diseja cadastrar mais filmes? (s/n): ").strip().lower()
    if continuar != "s":
        break

# Exibe os filmes cadastrados
print("\nFilmes cadastrados: ")
for filme in meus_filmes:
    print(filme)
print("-" *60)


    