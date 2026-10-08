precos = ["49.90", "120", "abc", "15.50"]

for texto in precos:
    try:
        preco = float(texto)
    except ValueError:
        print(f"O valor '{texto}' não é um preço válido.")
    else:
        preco_final = preco * 0.90
        print(f"Preço {preco:.2f} com 10% de desconto: {preco_final:.2f}")
