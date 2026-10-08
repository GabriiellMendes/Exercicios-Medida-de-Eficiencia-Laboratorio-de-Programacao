def calcular_media(n1, n2, n3):
    for nota in (n1, n2, n3):
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota inválida ({nota}): as notas devem estar entre 0 e 10.")

    return (n1 + n2 + n3) / 3


try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)
except ValueError as erro:
    print(f"Erro: {erro}")
else:
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Média: {media:.2f} - Situação: {situacao}")
