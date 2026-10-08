Valor_produto =  float(input("Valor da compra: "))

if Valor_produto >= 500:
    print(f"Você está apto para receber um desconto na sua compra de R$ {Valor_produto:.2f}")
else:
    print(f"Sua compra foi abaixo de R$ 500,00 e com isso você não recebe a promoção.")
