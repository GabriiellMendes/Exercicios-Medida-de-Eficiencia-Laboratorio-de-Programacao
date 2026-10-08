temperaturas = []

for i in range(5):
    temperaturas.append(float(input(f"Digite a temperatura média do {i+1}° dia: ")))

media = sum(temperaturas) / len(temperaturas)

print(f"Temperaturas cadastradas: {temperaturas}")
print(f"A média das temperaturas foi: {media:.2f}°C")

if 18 <= media <= 28:
    print("A média está dentro da faixa ideal de cultivo (18°C a 28°C).")
else:
    print("A média está fora da faixa ideal de cultivo (18°C a 28°C).")
