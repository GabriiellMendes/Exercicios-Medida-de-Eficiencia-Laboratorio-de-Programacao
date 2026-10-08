def ler_numeros():
    numeros = []
    for i in range(5):
        numeros.append(float(input(f"Digite o {i+1}° número: ")))
    return numeros


def maior_numero(numeros):
    maior = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
    return maior


def menor_numero(numeros):
    menor = numeros[0]
    for n in numeros:
        if n < menor:
            menor = n
    return menor


lista = ler_numeros()

print(f"Números informados: {lista}")
print(f"O maior número é: {maior_numero(lista)}")
print(f"O menor número é: {menor_numero(lista)}")
