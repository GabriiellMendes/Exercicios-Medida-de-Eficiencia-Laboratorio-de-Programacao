produtos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}° produto: ")
    quantidade = int(input(f"Digite a quantidade disponível de {nome}: "))
    produtos[nome] = quantidade

print("Produtos cadastrados:")
for nome, quantidade in produtos.items():
    print(f"{nome}: {quantidade} unidades")
