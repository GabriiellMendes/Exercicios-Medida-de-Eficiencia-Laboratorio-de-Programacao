def calcularCubo(numero):
    return numero ** 3


def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    else:
        return False


numero = int(input("Digite um número: "))
resultado = calcularDivisaoCubo(numero)

if resultado is False:
    print(f"{numero} não é divisível por 3, retorno: {resultado}")
else:
    print(f"{numero} é divisível por 3 e seu cubo é {resultado}")
