soma = 0
for i in range(10):
    produtos = int(input(f"Digite a quantidade de cestas básicas do {i+1}° voluntário: "))
    soma += produtos
print(f"A soma final das cestas básicas foi: {soma}")
