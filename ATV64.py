def somar_numeros(a, b, c):
    soma = a + b + c

    if soma <= 21:
        return soma

    if 11 in (a, b, c):
        soma -= 10

    if soma <= 21:
        return soma
    return -1


n1 = int(input("Digite o primeiro número (1 a 11): "))
n2 = int(input("Digite o segundo número (1 a 11): "))
n3 = int(input("Digite o terceiro número (1 a 11): "))

if not (1 <= n1 <= 11 and 1 <= n2 <= 11 and 1 <= n3 <= 11):
    print("Os números devem estar entre 1 e 11.")
else:
    print(f"Resultado: {somar_numeros(n1, n2, n3)}")
