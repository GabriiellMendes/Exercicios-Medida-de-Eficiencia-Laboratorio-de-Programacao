def seu_chico(cabecas, pernas):

    coelhos = (pernas - 2 * cabecas) / 2
    galinhas = cabecas - coelhos

    if coelhos < 0 or galinhas < 0 or coelhos != int(coelhos):
        return None

    return int(galinhas), int(coelhos)


cabecas = 35
pernas = 94

resultado = seu_chico(cabecas, pernas)

if resultado is None:
    print("Não existe solução para esses valores.")
else:
    galinhas, coelhos = resultado
    print(f"Seu Chico tem {galinhas} galinhas e {coelhos} coelhos.")
