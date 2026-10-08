notas = {
    "Ana": 8.5,
    "Carlos": 7.0,
    "Pedro": 6.5,
    "Beatriz": 9.0,
    "Maria": 5.5
}

print("Alunos disponíveis para consulta:")
for nome in notas:
    print(f"- {nome}")

aluno = input("Digite o nome do aluno que deseja consultar: ")

if aluno in notas:
    print(f"A nota de {aluno} é {notas[aluno]}")
else:
    print(f"O aluno {aluno} não está cadastrado.")
