alunos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

media_turma = sum(alunos.values()) / len(alunos)

print(f"A média da turma foi: {media_turma:.2f}")
print("Alunos aprovados:")

aprovados = 0
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} - nota {nota:.1f}")
        aprovados += 1

if aprovados == 0:
    print("Nenhum aluno foi aprovado.")
