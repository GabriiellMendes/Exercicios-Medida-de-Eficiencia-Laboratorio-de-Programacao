def menor_ou_maior(n1, n2):

    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1, n2)
    else:
        return max(n1, n2)


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f"Resultado: {menor_ou_maior(numero1, numero2)}")
