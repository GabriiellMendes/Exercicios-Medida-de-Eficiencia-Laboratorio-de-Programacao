medicamentos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i+1}° medicamento: ")
    quantidade = int(input(f"Digite a quantidade em estoque de {nome}: "))
    medicamentos[nome] = quantidade

consulta = input("Digite o nome do medicamento que deseja consultar: ")

if consulta in medicamentos:
    print(f"O medicamento {consulta} possui {medicamentos[consulta]} unidades em estoque.")
else:
    print(f"O medicamento {consulta} não está cadastrado.")
