alunos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

print("Alunos cadastrados:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.1f}")
