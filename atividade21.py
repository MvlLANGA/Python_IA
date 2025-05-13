graus_f = float(input("Qual a temperatura: "))
temperatura = (graus_f - 32)* 5/9
print(f"{temperatura:.1f}°")
if temperatura < 0:
    print("Brr, esta frio aqui!!")
else:
    print("*** Então ta OK ***")