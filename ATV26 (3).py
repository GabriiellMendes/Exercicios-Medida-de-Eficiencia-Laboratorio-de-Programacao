codigos = [1050, 2034, 3078, 4112, 5099]

codigo = int(input("Digite o código do produto que deseja verificar: "))

if codigo in codigos:
    print(f"O código {codigo} está presente na lista.")
else:
    print(f"O código {codigo} não foi encontrado na lista.")
