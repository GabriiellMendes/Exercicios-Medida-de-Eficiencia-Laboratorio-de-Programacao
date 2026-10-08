def parse_cpf(cpf):

    numeros = cpf.replace(".", "").replace("-", "")

    if not numeros.isdigit() or len(numeros) != 11:
        raise ValueError("CPF inválido: deve conter 11 dígitos numéricos.")

    return numeros


def main():
    cpf = input("Digite o CPF: ")

    try:
        cpf_limpo = parse_cpf(cpf)
    except ValueError as erro:
        print(f"Erro: {erro}")
    else:
        print(f"CPF válido: {cpf_limpo}")


main()
