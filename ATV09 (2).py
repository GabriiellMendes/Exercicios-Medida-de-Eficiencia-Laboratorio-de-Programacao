lista_livros = []
for i in range(1, 4):
    livros_lidos = input(f"Digite o {i}° livro mais emprestado do mês: ")
    lista_livros.append(livros_lidos)

print(f"Os livros mais emprestados do mês foram: {lista_livros[0]}, {lista_livros[1]} e {lista_livros[2]}.")
print(f"Lista cadastrada: {lista_livros}")
