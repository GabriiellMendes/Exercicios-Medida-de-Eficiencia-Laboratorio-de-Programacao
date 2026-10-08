soma = 0
for i in range(7):
    produtos = float(input(f"Digite o faturamento do {i+1}° dia: "))
    soma += produtos
print(f"O faturamento da semana foi R${soma:.2f}")
