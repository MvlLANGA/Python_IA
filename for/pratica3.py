string = "No momento estamos tentando viver um minuto de cada vez" # aqui adicionamos nossa string

def mais_caracteres(texto):
    maior_caracter = "" #Criamos uma variavel vazia
    maior_contagem = 0 #Criamos uma variavel pra contagem de caracteres

    for caracter in texto: 
        contagem = texto.count("") #Aqui contamos todos os caracteres da string
        if contagem > maior_contagem:
            maior_contagem = contagem
            maior_caracter = caracter
    return maior_caracter

print(mais_caracteres(string.replace("", "")))