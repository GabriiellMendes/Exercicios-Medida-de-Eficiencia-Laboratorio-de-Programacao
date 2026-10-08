nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade do funcionário: "))
setor = input("Digite o setor de atuação: ")

funcionario = {
    "nome": nome,
    "idade": idade,
    "setor": setor
}

print("Dados cadastrados:")
for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")
