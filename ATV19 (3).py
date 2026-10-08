numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1

if numero < 0:
    print("Fatorial só existe para números inteiros positivos.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é: {fatorial}")
