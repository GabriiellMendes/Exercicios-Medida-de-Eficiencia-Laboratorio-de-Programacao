Codigo_produto = int(input("Digite o codigo do equipamento: "))
if Codigo_produto % 2 == 0:
    print (f"O código {Codigo_produto} é par, esse equipamento é do setor administrativo.")
else:
    print (f"O código {Codigo_produto} é ímpar, esse equipamento é do setor operacional.")
