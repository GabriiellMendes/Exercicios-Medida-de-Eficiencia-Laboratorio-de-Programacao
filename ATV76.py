import traceback


def processar_lista(elementos):
    total = 0

    for elemento in elementos:
        try:
            numero = float(elemento)
            total += numero
        except (TypeError, ValueError):
            print(f"Elemento inválido: {elemento!r}")
            print(traceback.format_exc())
            continue

    return total


dados = [10, "20", "abc", None, 5.5, [1, 2], "7"]

print(f"Soma dos elementos válidos: {processar_lista(dados)}")
