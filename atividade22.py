salario = float(input("Quanto voce ganha por hora: "))
horas = int(input("Quantas horas voce trabalha por dia: "))
dia = int(input("Quantos dias da semana voce trabalha: "))
salario_diario = salario * horas
print(salario_diario)
if dia >= 6:
    total_semana = dia * salario_diario
    print(total_semana)
if dia >= 7:
    print(f"Voce ganha R${total_semana*2}se trabalhar aos domingos")


   

