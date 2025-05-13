prev_tempo = float(input("Qual a previsão do tempo para amanhã: "))

if prev_tempo >= 20:
    chuva = input("Vai chover s/n: ")
    if chuva == "s":
        print("Saia com roupas leves e Guarda chuva")
    else:
        print("Saia com roupas leves")

elif prev_tempo >= 10:
    chuva = input("Vai chover s/n: ")
    if chuva == "s":
        print("Leve uma Blusa e guarda chuva")
    else:
        print("Leve uma blusa leve")

elif prev_tempo >= 5 and prev_tempo < 10:
    chuva = input("Vai chover s/n: ")  
    if chuva == "s":
        print("Vai estar Frio leve casaco e guarda chuva")
    else:
        print("Saia bem agasalhado")
else:
    chuva = input("Vai chover s/n: ")
    if chuva == "s":
        print("Saia com muita Roupa e guarda chuva")
    else:
        print("Vai estar SUPER frio")    