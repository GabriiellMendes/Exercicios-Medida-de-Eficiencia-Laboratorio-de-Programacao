while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("A idade não pode ser menor que zero. Tente novamente.")
            continue

        break
    except ValueError:
        print("Valor inválido, digite apenas números inteiros. Tente novamente.")

print(f"Idade cadastrada com sucesso: {idade} anos")
