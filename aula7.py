#Voce importa essas bibliotecas
import re #Biblioteca re
import random #Biblioteca random
#Aqui voce busca a letra de A-Z maiusculo na senha ou o numero de 0-9 na palavra senha
print(re.search("[A-Z]", "Senha"))
print(re.search("[A-Z]", "seNHa"))
print(re.search("[0-9]", "Sen1ha"))
#Aqui voce usa o random pra escolher aleatoriamente um numero de 1-200
numero_secreto = random.randint(1,200)
print(numero_secreto)