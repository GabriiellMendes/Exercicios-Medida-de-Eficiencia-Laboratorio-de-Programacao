class SaldoInsuficienteError(Exception):
    pass


def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor do saque deve ser positivo.")

    if valor_saque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para o saque.")

    return saldo - valor_saque


saldo = 1000.00

try:
    valor = float(input(f"Seu saldo é R${saldo:.2f}. Digite o valor do saque: "))
    novo_saldo = realizar_saque(saldo, valor)
except ValueError as erro:
    print(f"Erro: {erro}")
except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")
else:
    print(f"Saque realizado com sucesso! Novo saldo: R${novo_saldo:.2f}")
