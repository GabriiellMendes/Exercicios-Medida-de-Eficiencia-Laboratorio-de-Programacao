setor1 = float(input("Digite o valor do consumo do setor 1: "))
setor2 = float(input("Digite o valor do consumo do setor 2: "))

if setor1 > setor2:
    print(f"O maior consumo de energia do mês foi do setor 1 com {setor1} kWh.")
elif setor2 > setor1:
    print(f"O maior consumo de energia do mês foi do setor 2 com {setor2} kWh.")
else:
    print(f"Os dois setores tiveram o mesmo consumo: {setor1} kWh.")
