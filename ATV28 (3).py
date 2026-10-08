periodos = ["manhã", "tarde", "noite", "madrugada"]
lista_temperaturas = []

for i in range(4):
    lista_temperaturas.append(float(input(f"Digite a temperatura média da {periodos[i]}: ")))

temperaturas = tuple(lista_temperaturas)

print(f"Temperaturas registradas: {temperaturas}")
print(f"A soma das temperaturas foi: {sum(temperaturas):.2f}°C")
