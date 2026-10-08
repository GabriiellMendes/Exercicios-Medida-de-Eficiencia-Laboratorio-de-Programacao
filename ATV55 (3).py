disciplinas = ("Matemática", "Português")
alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota_mat = float(input(f"Digite a nota de Matemática de {nome}: "))
    nota_port = float(input(f"Digite a nota de Português de {nome}: "))
    alunos[nome] = {"Matemática": nota_mat, "Português": nota_port}

print("Resultado dos alunos:")
for nome, notas in alunos.items():
    media = (notas["Matemática"] + notas["Português"]) / 2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"{nome} - média {media:.2f} - {situacao}")

print(f"Disciplinas cadastradas: {disciplinas}")
