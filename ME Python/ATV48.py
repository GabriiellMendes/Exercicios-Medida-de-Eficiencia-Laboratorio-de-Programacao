ordem = 3
identidade = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    identidade.append(linha)

print("Matriz identidade de ordem 3:")
for linha in identidade:
    print(linha)
