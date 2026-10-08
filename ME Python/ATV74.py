produtos = {
    1: {"nome": "Caderno", "preco": 15.90},
    2: {"nome": "Caneta", "preco": 3.50},
    3: {"nome": "Mochila", "preco": 120.00}
}


def rota_produto(id_produto):

    try:
        produto = produtos[id_produto]
        return 200, produto
    except KeyError:
        return 404, {"erro": "Produto não encontrado"}
    except Exception:

        return 500, {"erro": "Erro interno do servidor"}


print(rota_produto(1))
print(rota_produto(99))
print(rota_produto([1, 2]))
