nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print (f"Sua nota final foi {media:.2f} você foi aprovado")
else:
    print (f"Sua nota final foi {media:.2f} você foi reprovado, mais sorte da próxima vez.")
