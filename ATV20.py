satisfacao = 0
nota = 1

while nota != 0:
    nota = int(input("Digite uma nota (0 para encerrar): "))
    satisfacao += nota

print(f"A soma de todas as notas digitadas foi: {satisfacao}")
