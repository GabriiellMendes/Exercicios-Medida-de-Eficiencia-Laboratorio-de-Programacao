matriz = [
    [10, 20, 30],
    [15, 85, 35],
    [5, 8, 12]
]

maior = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print(f"O maior valor da matriz é: {maior}")
