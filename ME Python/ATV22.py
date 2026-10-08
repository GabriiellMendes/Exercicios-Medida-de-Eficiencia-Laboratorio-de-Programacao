notas = []

for i in range(5):
    notas.append(float(input(f"Digite a {i + 1}° nota: ")))

print("Todas as notas:", notas)
print("A maior nota:", max(notas))
