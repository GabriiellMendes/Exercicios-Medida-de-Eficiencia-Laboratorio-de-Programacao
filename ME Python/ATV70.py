def buscar_permissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except KeyError:
        print(f"Perfil '{perfil}' não existe.")
        return "acesso_restrito"
    except IndexError:
        print(f"O índice {indice} está fora dos limites das permissões de '{perfil}'.")
        return "acesso_restrito"


perfis = {
    "admin": ["ler", "escrever", "excluir"],
    "editor": ["ler", "escrever"],
    "visitante": ["ler"]
}

print(buscar_permissao(perfis, "admin", 2))
print(buscar_permissao(perfis, "editor", 1))
print(buscar_permissao(perfis, "visitante", 3))
print(buscar_permissao(perfis, "gerente", 0))
