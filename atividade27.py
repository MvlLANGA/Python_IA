categoria = float(input("Qual o valor do produto: "))
if categoria >0 and categoria <=50:
    print("Categoria Economica")
elif categoria > 50 and categoria <= 100:
    print("Categoria Intermediaria")
else:
    print("Categoria Premium")
