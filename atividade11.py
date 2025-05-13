capital_inicial = float(input("Qual o capital inicial: "))
taxa_juros_anual = float(input("Qual a taxa de juros anual: "))
tempo_anos = int(input("Tempo em anos: "))
juros = capital_inicial*taxa_juros_anual*tempo_anos
print(f"O seu capital inicial: {capital_inicial} \nA taxa de juros anual: {taxa_juros_anual} \nTempo em anos: {tempo_anos} \nO montante final: {juros}")