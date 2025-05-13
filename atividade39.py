from math import sqrt
while True:
    num = int(input("Escolha um numero: "))
    if num > 0:
        print(sqrt(num))
    elif num == 0:
        print("BREAk")
        break
    else:
        print("--- Numero Inalido ---")
     

