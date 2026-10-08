matriz = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 8, 12]
]

soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor

print(f"A soma de todos os valores da matriz é: {soma}")
