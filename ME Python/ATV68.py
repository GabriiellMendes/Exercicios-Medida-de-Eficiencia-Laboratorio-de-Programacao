try:
    lucros = float(input("Digite o lucro do trimestre: "))
    acionistas = int(input("Digite a quantidade de acionistas: "))

    divisao = lucros / acionistas
except ZeroDivisionError:
    print("Erro: a quantidade de acionistas não pode ser zero.")
except ValueError:
    print("Erro: digite apenas valores numéricos.")
else:
    print(f"Cada acionista receberá R${divisao:.2f}")
