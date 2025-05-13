nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
media = (nota1 + nota2)/2
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")