try:
    def maior():
        with  open("numeros.txt") as arquivo:
            maior =0
            for linha in arquivo:
                numero = int(linha)
                if numero > maior:
                    maior = numero
            print("Maior numero:", maior)
    
   
except FileNotFoundError:
    print("Arquivo não encontrado")

except ValueError:
    print("ERRO: o arquivo contem dados que não são numeros inteiros") 
maior()