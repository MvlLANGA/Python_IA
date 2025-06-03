#try: # tudo oq esta aqui dentro do Try pode gerar um tipo de erro
#    numero = int(input("Digite um numero: "))
#    print(f"Voce digitou: {numero}")

#except ValueError:
#    print("Erro: Você digitou o valor errado!!")

#try:
#    num_str = input("Digite um numero: ")
#    num_int = int(num_str)

#    resultado = 10/num_int
#    print(f"10 dividido por {num_int} é {resultado}")

#except ValueError:
#    print("ERRO: Entrada Invalida!!! Por favor, digite um numero")

#except ZeroDivisionError:
#    print("ERRO: Não é possivel dividir por zero")

#except Exception as e:
#    print(f"Ocorreu um erro inesperado {e}")

#else: # Quando não teve nenhuma exceção
#    print("Deu certo")

# Executa mesmo que tenha um erro ou não no try
#finally: # Continua a correr o scrypt
#    if num_int == 0:
#        num_int = int(input("Digite um numero: "))
#        num_str = input("Digite um numero: ")

arquivo = None
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print("Arquivo lido com sucesso")

except FileNotFoundError:
    print("ERRO: Arquivo não encontrado")

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

else:
    print("Processamento do arquivo concluido com sucesso")

finally:
    if arquivo:
        arquivo.close()
        print("Arquivo fechado")

        