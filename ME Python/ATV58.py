def calcular_gorjeta(valor_conta):
    gorjeta = valor_conta * 0.10
    print(f"A gorjeta do garçom (10%) é de R${gorjeta:.2f}")


conta = float(input("Digite o valor da conta do restaurante: "))
calcular_gorjeta(conta)
