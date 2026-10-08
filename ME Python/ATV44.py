matriz = [
    [450, 320, 780],
    [215, 85, 635],
    [590, 148, 412]
]

menor = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor < menor:
            menor = valor

print(f"O menor custo registrado foi: R${menor}")
