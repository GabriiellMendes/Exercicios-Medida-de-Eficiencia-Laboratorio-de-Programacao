def contar_caractere(texto, caractere):
    quantidade = 0
    for letra in texto:
        if letra == caractere:
            quantidade += 1
    return quantidade


texto = input("Digite uma string: ")
caractere = input("Digite o caractere que deseja contar: ")

if len(caractere) != 1:
    print("Digite apenas um caractere.")
else:
    total = contar_caractere(texto, caractere)
    print(f"O caractere '{caractere}' aparece {total} vez(es) na string.")
