soma = []
for i in range(4):
    gastos = float(input(f"Os gasto da {i+1}° semana: "))
    soma.append(gastos)

total = sum(soma)

print(f"O gasto mensal foi R${total:.2f}")
