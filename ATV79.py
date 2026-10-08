def cadastrar_produto(nome, preco, quantidade):
    if nome.strip() == "":
        raise ValueError("O nome do produto não pode ser vazio.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return f"Produto '{nome}' cadastrado com sucesso! Preço: R${preco:.2f} | Quantidade: {quantidade}"


try:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    mensagem = cadastrar_produto(nome, preco, quantidade)
except ValueError as erro:
    print(f"Erro: {erro}")
else:
    print(mensagem)
