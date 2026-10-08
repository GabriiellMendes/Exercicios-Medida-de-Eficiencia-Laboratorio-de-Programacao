participantes = []

for i in range(5):
    participantes.append(input(f"Digite o nome do {i+1}° participante na ordem de chegada: "))

print(f"Ordem de chegada: {participantes}")

participantes.reverse()

print(f"Ordem inversa: {participantes}")
