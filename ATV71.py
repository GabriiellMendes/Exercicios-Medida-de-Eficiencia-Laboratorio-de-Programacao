class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(f"Saldo insuficiente: saldo R${saldo:.2f}, saque de R${valor:.2f}")
    return saldo - valor


saldo = 500.00
valor_saque = float(input(f"Seu saldo é R${saldo:.2f}. Digite o valor do saque: "))

try:
    saldo = sacar(saldo, valor_saque)
except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")
else:
    print(f"Saque realizado! Novo saldo: R${saldo:.2f}")
