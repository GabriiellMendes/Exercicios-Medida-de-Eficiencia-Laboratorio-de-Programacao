matriz = [
    [5, -3, 0],
    [-8, 12, 7],
    [-1, 4, -6]
]

positivos = 0
for linha in matriz:
    for valor in linha:
        if valor > 0:
            positivos += 1

print(f"A matriz possui {positivos} valores positivos.")
