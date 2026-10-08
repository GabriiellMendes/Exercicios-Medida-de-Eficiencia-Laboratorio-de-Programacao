alimentos = 0

for i in range(5):
    quantidade_alim = int(input(f"Quantidade de alimentos arrecadados pelo {i+1}° voluntário: "))
    alimentos += quantidade_alim

print(f"O total de alimentos arrecadados foram: {alimentos}")
