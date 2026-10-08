try:
    arquivo = open("relatorio_vendas.txt", "r", encoding="utf-8")
    print(arquivo.read())
    arquivo.close()
except FileNotFoundError:
    print("Erro: o arquivo relatorio_vendas.txt não foi encontrado.")
finally:
    print("Encerrando o uso do recurso.")
